from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from warehouse.views import show_genres

urlpatterns = [
    path('genres/', show_genres),

]