from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from warehouse.forms import AddMaterialForm
from warehouse.models import Material


class MaterialCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'title',
                   # 'color'
                   ]
   form = AddMaterialForm
   list_filter = ['category',
                  # 'color'
                  ]
   search_fields = ['category', 'title',
                    # 'color'
                    ]


admin.site.register(Material, MaterialCreateAdmin)

