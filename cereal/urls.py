from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cereal_catalog, name="cereal-index"),
    path('<int:id>', views.get_cereal_by_id, name="cereal-details"),
    path('create_cereal', views.create_cereal, name="create-cereal"),
    path('delete_cereal/<int:id>', views.delete_cereal, name="delete-cereal"),
    path('update_cereal/<int:id>', views.update_cereal, name="update-cereal")
]