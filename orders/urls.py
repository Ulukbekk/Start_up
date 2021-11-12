from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from orders.views import order_detail, order_edit, home_page, status_sort, worker_sort, condition_sort, \
    order_sort, worker_edit, add_order, worker_detail

urlpatterns = [
    # path('complete-order/<int:pk>/', complete_order, name='complete_order'),
    path('order-detail/<int:pk>/', order_detail, name='order_detail'),
    path('worker-detail/<int:pk>/', worker_detail, name='worker_detail'),
    path('order-edit/<int:pk>/', order_edit, name='order_edit'),
    path('worker-edit/<int:pk>/', worker_edit, name='worker_edit'),
    path('condition-sort/<int:pk>/', condition_sort, name='condition_sort'),
    path('worker-sort/<int:pk>/', worker_sort, name='worker_sort'),
    path('status-sort/<int:pk>/', status_sort, name='status_sort'),
    path('order-sort/<int:pk>/', order_sort, name='order_sort'),
    path('add-order/', add_order, name='add_order'),
    # path('upload/', files, name='upload'),
    # path('download/', download, name='downlaod'),
    # path('download_file/<int:pk>/', download_files, name='download_file'),
    path('home/', home_page, name='home_page'),
]
