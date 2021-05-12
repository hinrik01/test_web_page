from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home-index"),
    path('about_us/', views.about_us, name="about_us"),
    path('contact/', views.contact, name="contact"),
    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
    path('terms/', views.terms, name="terms"),
]
