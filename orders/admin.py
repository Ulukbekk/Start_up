from django.contrib import admin

from orders.forms import OrderSearchForm
from orders.models import ManagerBlank


# @admin.register(ManagerBlank)
class Orders(admin.ModelAdmin):
    list_display = ['author', 'title',
                    'client', 'deadline',
                    'status', 'price',
                    'condition']
    form = OrderSearchForm
    list_filter = ['author', 'condition', 'status']
    search_fields = ['title', 'client', 'author', 'status', 'condition', 'worker', 'order', 'deadline']


admin.site.register(ManagerBlank, Orders)