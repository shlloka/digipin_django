
from django.urls import path
from .views import get_digipin 
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),  # now '/' shows home.html
    path('get_digipin/', views.get_digipin, name='get_digipin'),  # API endpoint
    path('bookings/', views.bookings_view, name='bookings'),  # Bookings page
]

