from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView

# from common.views import TitleMixin
from accounts.forms import UserOurRegistration, UserProfileForm


class SignUP(generic.CreateView):
    form_class = UserOurRegistration
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'registration/profile.html'
    title = 'Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('accounts:profile', kwargs={'pk': self.object.pk})

