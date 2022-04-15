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
            'save_title_wasted_material_one', 'save_amount_wasted_material_one', 'save_remainder_wasted_material_one',
            'save_title_wasted_material_two', 'save_amount_wasted_material_two', 'save_remainder_wasted_material_two',
            'save_title_wasted_material_three', 'save_amount_wasted_material_three', 'save_remainder_wasted_material_three',
            'save_title_wasted_material_four', 'save_amount_wasted_material_four', 'save_remainder_wasted_material_four',
            'save_title_wasted_material_five', 'save_amount_wasted_material_five', 'save_remainder_wasted_material_five',
            'save_title_wasted_material_six', 'save_amount_wasted_material_six', 'save_remainder_wasted_material_six',
            'save_title_wasted_material_seven', 'save_amount_wasted_material_seven', 'save_remainder_wasted_material_seven',
            'save_title_wasted_material_eight', 'save_amount_wasted_material_eight', 'save_remainder_wasted_material_eight',
            'save_title_wasted_material_nine', 'save_amount_wasted_material_nine', 'save_remainder_wasted_material_nine',
            'save_title_wasted_material_ten', 'save_amount_wasted_material_ten', 'save_remainder_wasted_material_ten',
            'save_title_wasted_material_eleven', 'save_amount_wasted_material_eleven', 'save_remainder_wasted_material_eleven',
            'save_title_wasted_material_twelve', 'save_amount_wasted_material_twelve', 'save_remainder_wasted_material_twelve',
            'save_title_wasted_material_thirteen', 'save_amount_wasted_material_thirteen', 'save_remainder_wasted_material_thirteen',
            'save_title_wasted_material_fourteen', 'save_amount_wasted_material_fourteen', 'save_remainder_wasted_material_fourteen',
            'save_title_wasted_material_fifteen', 'save_amount_wasted_material_fifteen', 'save_remainder_wasted_material_fifteen',
            'save_title_wasted_material_sixteen', 'save_amount_wasted_material_sixteen', 'save_remainder_wasted_material_sixteen',
            'save_title_wasted_material_seventeen', 'save_amount_wasted_material_seventeen', 'save_remainder_wasted_material_seventeen',
            'save_title_wasted_material_eighteen', 'save_amount_wasted_material_eighteen', 'save_remainder_wasted_material_eighteen',
            'save_title_wasted_material_nineteen', 'save_amount_wasted_material_nineteen', 'save_remainder_wasted_material_nineteen',
            'save_title_wasted_material_twenty', 'save_amount_wasted_material_twenty', 'save_remainder_wasted_material_twenty',
    )


admin.site.register(ManagerBlank, Orders)


@admin.register(ManagerBlankFiles)
class ManagerBlankFilesAdmin(admin.ModelAdmin):
    list_display = ['order', 'files']