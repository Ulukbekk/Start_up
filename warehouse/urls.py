from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from warehouse.views import add_material, add_category, all_materials, update_material

urlpatterns = [
    path('update-material/<int:pk>/', update_material, name='update_material'),
    path('all-materials/', all_materials, name='all_materials'),
    path('add-material/', add_material, name='add_material'),
    path('add-category/', add_category, name='add_category'),
]