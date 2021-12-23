from django import forms

from warehouse.models import Material, Category


class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'category',
            'title',
            'remainder',
            'amount',
            'color',
            'shade',
        )


class UpdateMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'category',
            'title',
            'remainder',
            'amount',
            'color',
            'shade',
        )


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class MaterialSearchForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
             'category', 'title',
            'color', 'shade'
        )