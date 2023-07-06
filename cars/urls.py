from django.urls import path
from .views import HomePage, AllCarsBrand, CarDetailView, CarReviewView, NewCarsView, UsedCarsView

app_name = 'cars'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('cars/new/', NewCarsView.as_view(), name='new_cars'),
    path('cars/used/', UsedCarsView.as_view(), name='used_cars'),
    path('cars/<slug:cars_brand>/', AllCarsBrand.as_view(), name='all_cars_brand'),
    path('cars/<slug:cars_brand>/<slug:model_name>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<slug:cars_brand>/<slug:model_name>/reviews', CarReviewView.as_view(), name='car_reviews'),

]
