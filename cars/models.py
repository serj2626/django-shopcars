from django.db import models
from django.contrib.auth.models import User


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

    likes = models.IntegerField(verbose_name='кол-во лайков', default=0)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} года'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class CarImage(models.Model):
    model = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='модель', related_name='all_images')
    photo1 = models.ImageField(verbose_name='Фото1', upload_to='media/cars/', blank=True)
    photo2 = models.ImageField(verbose_name='Фото2', upload_to='media/cars/', blank=True)
    photo3 = models.ImageField(verbose_name='Фото3', upload_to='media/cars/', blank=True)
    photo4 = models.ImageField(verbose_name='Фото4', upload_to='media/cars/', blank=True)
    photo5 = models.ImageField(verbose_name='Фото5', upload_to='media/cars/', blank=True)
    photo6 = models.ImageField(verbose_name='Фото6', upload_to='media/cars/', blank=True)

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
