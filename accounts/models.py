from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name='имя', max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name='фамилия', max_length=100, blank=True, null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='media/profile/default-profile.png')
    bio = models.TextField('Биография', blank=True, null=True)

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('accounts:profile', kwargs={'name': self.user.username})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
