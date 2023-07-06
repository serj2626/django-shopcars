# Generated by Django 4.2.2 on 2023-07-05 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Бренд')),
                ('image', models.ImageField(upload_to='brands/', verbose_name='Эмблема')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, unique=True, verbose_name='Модель')),
                ('year', models.PositiveIntegerField(default=2022, verbose_name='Год выпуска')),
                ('color', models.CharField(choices=[('Red', ' Красный'), ('White', ' Белый'), ('Yellow', ' Желтый'), ('Black', ' Черный'), ('Blue', ' Синий'), ('Silver', ' Серебристый'), ('Green', ' Зеленый'), ('Grey', 'Серый')], max_length=100, verbose_name='цвет')),
                ('drive_unit', models.CharField(choices=[('Front', ' Передний'), ('Back', ' Задний'), ('Full', ' Полный')], max_length=100, verbose_name='привод')),
                ('hp', models.PositiveSmallIntegerField(default=100, verbose_name='Л.С.')),
                ('mileage', models.PositiveIntegerField(default=0, help_text='введите пробег в километрах', verbose_name='пробег')),
                ('price', models.DecimalField(decimal_places=2, default=100, help_text='Введите цену в рублях', max_digits=14, verbose_name='цена')),
                ('img', models.ImageField(blank=True, upload_to='cars/', verbose_name='Постер')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('country', models.CharField(choices=[('China', ' Китай'), ('Germany', ' Германия'), ('Russia', ' Россия'), ('Japan', ' Япония'), ('Korea', ' Корея'), ('France', ' Франция'), ('Sweden', ' Швеция')], default='China', max_length=100, verbose_name='страна производства')),
                ('transmission', models.CharField(choices=[('Robot', ' Робот'), ('Variator', ' Вариатор'), ('Automatic', ' Автоматическая'), ('Manual', ' Ручная')], default='Automatic', max_length=100, verbose_name='коробка передач')),
                ('likes', models.IntegerField(default=0, verbose_name='кол-во лайков')),
                ('slug', models.SlugField(unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_cars', to='cars.brand', verbose_name='бренд')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=33, verbose_name='Состояние')),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Состояние',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='отзыв')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата отзыва')),
                ('likes', models.IntegerField(default=0, verbose_name='кол-во лайков')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models_reviews', to='cars.car', verbose_name='Модель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_reviews', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(blank=True, upload_to='media/cars/', verbose_name='Фото1')),
                ('photo2', models.ImageField(blank=True, upload_to='media/cars/', verbose_name='Фото2')),
                ('photo3', models.ImageField(blank=True, upload_to='media/cars/', verbose_name='Фото3')),
                ('photo4', models.ImageField(blank=True, upload_to='media/cars/', verbose_name='Фото4')),
                ('photo5', models.ImageField(blank=True, upload_to='media/cars/', verbose_name='Фото5')),
                ('photo6', models.ImageField(blank=True, upload_to='media/cars/', verbose_name='Фото6')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_images', to='cars.car', verbose_name='модель')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='condition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.condition', verbose_name='Состояние'),
        ),
    ]
