from stockmgmt.views import home, list_item, add_items, update_items, delete_items
from django.urls import path

urlpatterns = [
	path('', home, name='stock'),
    path('list_item/', list_item, name='list_items'),
    path('add_items/', add_items, name='add_items'),
    path('update_items/<str:pk>/', update_items, name="update_items"),
    path('delete_items/<str:pk>/', delete_items, name="delete_items"),
    ]