from django.contrib import admin

from orders.forms import OrderSearchForm
from orders.models import ManagerBlank, ManagerBlankFiles


class Orders(admin.ModelAdmin):
    list_display = ['author', 'title',
                    'client', 'deadline',
                    'status', 'price',
                    'condition']
    form = OrderSearchForm
    list_filter = ['author', 'condition', 'status']
    search_fields = ['title', 'client', 'author', 'status', 'condition', 'worker', 'order', 'deadline']
    fields = (
            'title',
            'description',
            'deadline',
            'client',
            'amount',
            'price',
            'order',
            'condition',
            'worker',
            'wasted_material_one',
            'amount_wasted_material_one',
            'wasted_material_two',
            'amount_wasted_material_two',
            'wasted_material_three',
            'amount_wasted_material_three',
            'wasted_material_four',
            'amount_wasted_material_four',
            'wasted_material_five',
            'amount_wasted_material_five',
            'wasted_material_six',
            'amount_wasted_material_six',
            'wasted_material_seven',
            'amount_wasted_material_seven',
            'wasted_material_eight',
            'amount_wasted_material_eight',
            'print',
            'design',
            'machine',
    )


admin.site.register(ManagerBlank, Orders)


@admin.register(ManagerBlankFiles)
class ManagerBlankFilesAdmin(admin.ModelAdmin):
    list_display = ['order', 'files']