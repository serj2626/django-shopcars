from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from cars.forms import ReviewsForm
from .forms import FeedBackForm, ReviewsForm
from .models import Brand, Car, Reviews
from django.contrib import messages


class HomePage(ListView):
    '''Домашняя страница'''
    model = Car
    template_name = 'cars/home_page.html'
    context_object_name = 'cars'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class NewCarsView(ListView):
    '''Новые автомобили'''
    model = Car
    template_name = 'cars/new_cars.html'
    context_object_name = 'cars'
    paginate_by = 9
    queryset = Car.objects.filter(condition_id=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новые авто'
        return context


class UsedCarsView(ListView):
    '''Авто с пробегом'''
    model = Car
    template_name = 'cars/used_cars.html'
    context_object_name = 'cars'
    paginate_by = 9
    queryset = Car.objects.filter(condition_id=2)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Б/У Авто'
        return context


class AllCarsBrand(DetailView):
    '''Все авто определенного бренда'''

    model = Brand
    template_name = 'cars/all_cars_brand.html'
    slug_url_kwarg = 'cars_brand'
    context_object_name = 'brand'


class CarDetailView(View):
    '''Автомобиль'''

    def get(self, request, cars_brand, model_name, number):
        # car = Brand.objects.get(slug=cars_brand).all_cars.all().get(slug=model_name)

        car = Car.objects.select_related('brand').get(slug=model_name, ad_number=number)
        images = car.all_images.all()
        context = {
            'car': car,
            'images': images
        }
        return render(request, 'cars/car_detail.html', context)


class CarReviewView(View):
    '''Автомобиль'''

    def get(self, request, cars_brand, model_name, number):
        car = Brand.objects.get(slug=cars_brand).all_cars.all().get(slug=model_name, ad_number=number)
        all_reviews = car.models_reviews.all().order_by('-create_date')
        form = ReviewsForm()

        paginator = Paginator(all_reviews, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'car': car,
            'form': form,
            'all_reviews': all_reviews,
            'page_obj': page_obj
        }
        return render(request, 'cars/car_reviews.html', context)

    def post(self, request, cars_brand, model_name):
        car = Brand.objects.get(slug=cars_brand).all_cars.all().get(slug=model_name)
        form = ReviewsForm(request.POST)

        if form.is_valid():
            text = request.POST['text']
            user = self.request.user
            car = Brand.objects.get(slug=cars_brand).all_cars.all().get(slug=model_name)
            Reviews.objects.create(model=car, user=user, text=text)
            messages.success(request, f'Ваш отзыв об автомобиле {car} успешно отправлен')
            return redirect('cars:home')


class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'cars/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['serj2626@mail.ru'])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('cars: success')
        return render(request, 'cars/contact.html', context={
            'form': form,
        })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cars/success.html', context={
            'title': 'Спасибо'
        })


def addlike(request, model_name, number):
    '''Поставить лайк'''
    car = Car.objects.select_related('brand').get(slug=model_name, ad_number=number)
    car.likes += 1
    car.save()
    return redirect('/')
