from django.contrib import admin
from users.models import Account, Client, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['position', 'id']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'position', 'phone']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'organization', 'amount_orders', 'status']


