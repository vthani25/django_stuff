from django.urls import path
from . import views

urlpatterns = [
    path('translate/', views.translate),
    path('translate_bulk/', views.translate_bulk),
]
