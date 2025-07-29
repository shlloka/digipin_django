from django.urls import path
from . import views

urlpatterns = [
    path('get_digipin/', views.get_digipin, name='get_digipin'),
]
