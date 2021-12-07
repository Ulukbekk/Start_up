from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import register, add_client, list_clients, profile, client_detail, client_edit, change_password

urlpatterns = [
    path('registration/', register, name='registration'),
    path('add-client/', add_client, name='add_client'),
    path('client-detail/<int:pk>/', client_detail, name='client_detail'),
    path('client-edit/<int:pk>/', client_edit, name='client_edit'),
    path('list-clients/', list_clients, name='list_clients'),
    path('profile/', profile, name='profile'),
    path('', LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='users/logout.html'
    ), name='logout'),
    url(r'^password/$', change_password, name='change_password'),
]