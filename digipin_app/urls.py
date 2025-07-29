# from django.urls import path
# from . import views

# urlpatterns = [
#     path('get_digipin/', views.get_digipin, name='get_digipin'),
# ]

# digipin_app/urls.py
from django.urls import path
from .views import get_digipin 

urlpatterns = [
    path('', get_digipin, name='get_digipin'),
]

