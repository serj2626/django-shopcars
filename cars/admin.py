from django.contrib import admin
from .models import Condition, Brand, Car, CarImage, Reviews


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'condition', 'year', 'price', 'color', 'drive_unit', 'hp', 'quantity')
    ordering = ('year',)
    prepopulated_fields = {'slug': ('model',)}


admin.site.register(CarImage)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'create_date', 'likes')
