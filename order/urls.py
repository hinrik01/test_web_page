from django.urls import path
from . import views

urlpatterns = [
    path('payment', views.payment, name="payment-step"),
    path('review', views.review, name="review-step"),
    path('confirmation', views.confirmation, name="confirmation-step"),
]
