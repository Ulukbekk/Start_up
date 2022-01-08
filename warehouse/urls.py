from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from warehouse.views import add_material, all_materials, update_material, material_detail, issue_items, receive_items

urlpatterns = [
    path('material-detail/<int:pk>/', material_detail, name='material_detail'),
    path('update-material/<int:pk>/', update_material, name='update_material'),
    path('receive-items/<str:pk>/', receive_items, name='receive_items'),
    path('issue-items/<str:pk>/', issue_items, name='issue_items'),
    path('all-materials/', all_materials, name='all_materials'),
    path('add-material/', add_material, name='add_material'),
]
