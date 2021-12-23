from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from warehouse.forms import AddMaterialForm
from warehouse.models import Category, Material


class MaterialCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'title', 'color', 'shade']
   form = AddMaterialForm
   list_filter = ['category', 'color', 'shade']
   search_fields = ['category', 'title', 'color', 'shade']


admin.site.register(Material, MaterialCreateAdmin)
admin.site.register(Category)

