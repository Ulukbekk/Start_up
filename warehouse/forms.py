from django import forms

from warehouse.models import Material


class AddMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'category',
            'title',
            'remainder',
            'amount',
        )


class UpdateMaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'category',
            'title',
            'remainder',
            'amount',
            # 'color',
        )


class MaterialSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Material
        fields = (
             'category', 'title',
        )


class IssueForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('issue_quantity',
                  'remainder')


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('receive_quantity',
                  'remainder')