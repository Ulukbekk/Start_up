from django.contrib import admin

from users.forms import AddClientForm, SearchClientForm
from users.models import Account, Client


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'position', 'phone']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'organization', 'amount_orders', 'status']
    form = SearchClientForm
    list_filter = ['first_name', 'organization', 'status']
    search_fields = ['first_name', 'last_name', 'phone', 'status']


admin.site.register(Client, ClientAdmin)

