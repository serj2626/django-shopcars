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
    list_display = (
        'brand', 'model', 'condition', 'year', 'price', 'color', 'hp', 'quantity', 'ad_number', 'stock')
    ordering = ('brand',)
    prepopulated_fields = {'slug': ('model',)}
    list_editable = ('year', 'price', 'hp', 'quantity', 'color', 'ad_number')
    list_per_page = 10
    actions = ('set_stock', 'set_no_stock')

    @admin.action(description='Установить статус - авто в наличии')
    def set_stock(self, request, queryset):
        queryset.update(stock=True)

    @admin.action(description='Установить статус - авто не в наличии')
    def set_no_stock(self, request, queryset):
        queryset.update(stock=False)


admin.site.register(CarImage)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'create_date', 'likes')
