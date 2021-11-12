from django.contrib import admin
from orders.models import ManagerBlank, Status, Condition, Worker, Order, Order_file


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['status', 'id']


@admin.register(Condition)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['condition', 'id']


@admin.register(Worker)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['worker', 'id']


@admin.register(Order)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['order', 'id']


@admin.register(Order_file)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['order', 'files', 'id']


@admin.register(ManagerBlank)
class Orders(admin.ModelAdmin):
    list_display = ['author', 'title',
                    'client', 'deadline',
                    'status', 'price',
                    'condition']
