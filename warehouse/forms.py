from django import forms

from warehouse.models import Material


class AddMaterial(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'sub_category',
            'size',
            'amount',
            'color',
            'shade',
        )
