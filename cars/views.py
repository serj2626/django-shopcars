from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Condition, Brand, Car


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

    def get(self, request, cars_brand, model_name):
        car = Brand.objects.get(slug=cars_brand).all_cars.all().get(slug=model_name)
        context = {'car': car}
        return render(request, 'cars/car_detail.html', context)


class CarReviewView(View):
    '''Автомобиль'''

    def get(self, request, cars_brand, model_name):
        car = Brand.objects.get(slug=cars_brand).all_cars.all().get(slug=model_name)
        context = {'car': car}
        return render(request, 'cars/car_reviews.html', context)
