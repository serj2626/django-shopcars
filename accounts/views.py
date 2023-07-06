from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import UserOurRegistration


class SignUP(generic.CreateView):
    form_class = UserOurRegistration
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/signup.html'
