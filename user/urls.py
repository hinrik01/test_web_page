from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.view_profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('profile/edit-address', views.edit_address, name='edit-address'),
    path('order-history', views.order_history, name='order-history'),
    path('delete_address', views.delete_address, name='delete-address'),
    path('search_history', views.search_history, name='search-history')
]
