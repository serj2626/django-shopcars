from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Condition(models.Model):
    title = models.CharField(max_length=33, verbose_name='Состояние')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояние'


class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name='Бренд', unique=True)
    image = models.ImageField(verbose_name='Эмблема', upload_to='brands/')
    description = models.TextField(verbose_name='описание', blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ('title',)


class Car(models.Model):

    COLORS = [
        ('Red', ' Красный'),
        ('White', ' Белый'),
        ('Yellow', ' Желтый'),
        ('Black', ' Черный'),
        ('Blue', ' Синий'),
        ('Silver', ' Серебристый'),
        ('Green', ' Зеленый'),
        ('Grey', 'Серый')
    ]

    DRIVE = [
        ('Front', ' Передний'),
        ('Back', ' Задний'),
        ('Full', ' Полный'),
    ]

    COUNTRY = [
        ('China', ' Китай'),
        ('Germany', ' Германия'),
        ('Russia', ' Россия'),
        ('Japan', ' Япония'),
        ('Korea', ' Корея'),
        ('France', ' Франция'),
        ('Sweden', ' Швеция'),
    ]

    TRANSMISSION = [
        ('Robot', ' Робот'),
        ('Variator', ' Вариатор'),
        ('Automatic', ' Автоматическая'),
        ('Manual', ' Ручная'),
    ]

    model = models.CharField(max_length=100, verbose_name='Модель', unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='бренд', related_name='all_cars')
    condition = models.ForeignKey(Condition, verbose_name='Состояние', on_delete=models.CASCADE)
    year = models.PositiveIntegerField(verbose_name='Год выпуска', default=2022)
    color = models.CharField(max_length=100, verbose_name='цвет', choices=COLORS)
    drive_unit = models.CharField(max_length=100, verbose_name='привод', choices=DRIVE)
    hp = models.PositiveSmallIntegerField(verbose_name='Л.С.', default=100)
    mileage = models.PositiveIntegerField(verbose_name='пробег', default=0, help_text='введите пробег в километрах')
    price = models.DecimalField(verbose_name='цена', default=100, max_digits=14, decimal_places=2,
                                help_text='Введите цену в рублях')
    description = models.TextField(verbose_name='описание', blank=True)
    img = models.ImageField(verbose_name='Постер', upload_to='cars/', blank=True)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество', default=0)
    country = models.CharField(max_length=100, verbose_name='страна производства', choices=COUNTRY, default='China')
    transmission = models.CharField(max_length=100, verbose_name='коробка передач', choices=TRANSMISSION,
                                    default='Automatic')
    ad_number = models.IntegerField(verbose_name='номер объявления', unique=True, default=None)
    likes = models.IntegerField(verbose_name='кол-во лайков', default=0)
    stock = models.BooleanField(verbose_name='наличие', default=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def get_absolute_url(self):
        return reverse('cars:car_detail', kwargs={'cars_brand': self.brand.slug, 'model_name': self.slug, 'number': self.ad_number})

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} года'

    def clean(self):
        if 0 > self.likes:
            raise ValidationError('Кол-во лайков не может быть отрицательнм')

    def save(self, *args, **kwargs):
        self.clean()

        if self.quantity > 0:
            self.stock = True
        else:
            self.stock = False
        super().save(*args, **kwargs)


class CarImage(models.Model):
    model = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='модель', related_name='all_images')
    image = models.ImageField(verbose_name='Картинка', upload_to='cars/', blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'Фотки {self.model}'


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='users_reviews')
    model = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Модель', related_name='models_reviews')
    text = models.TextField(blank=True, verbose_name='отзыв')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата отзыва')
    likes = models.IntegerField(verbose_name='кол-во лайков', default=0)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-create_date']

    def __str__(self):
        return f'Отзыв от пользоваетля {self.user.username} созданный {self.create_date}'
