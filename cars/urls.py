from django.urls import path
from .views import HomePage, AllCarsBrand, CarDetailView, CarReviewView, NewCarsView, UsedCarsView, FeedBackView, \
    SuccessView, addlike

app_name = 'cars'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('cars/new/', NewCarsView.as_view(), name='new_cars'),
    path('cars/used/', UsedCarsView.as_view(), name='used_cars'),
    path('cars/<slug:cars_brand>/', AllCarsBrand.as_view(), name='all_cars_brand'),
    path('cars/<slug:cars_brand>/<slug:model_name>/<int:number>', CarDetailView.as_view(), name='car_detail'),
    path('cars/<slug:cars_brand>/<slug:model_name>/<int:number>/reviews', CarReviewView.as_view(), name='car_reviews'),
    path('cars/<slug:cars_brand>/<slug:model_name>/<int:number>/addlike', addlike, name='add_like'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),

]
