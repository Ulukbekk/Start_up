from django import forms
from django.core.exceptions import ValidationError

from orders.models import ManagerBlank, ManagerBlankFiles


class ManagerBlankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['condition'].empty_label = "Не начато"
        self.fields['worker'].empty_label = "Не выбран"
        self.fields['order'].empty_label = "Не выбрано"
        self.fields['client'].empty_label = "Не выбран"

    class Meta:
        model = ManagerBlank
        fields = [
            'title',
            'description',
            'deadline',
            'client',
            # 'status',
            'amount',
            'price',
            'order',
            'condition',
            'worker',
        ]
        widgets = {'deadline': forms.DateInput(attrs={'id': 'davaToday', 'type': 'date'}),
                    # 'files': forms.ClearableFileInput(attrs={'class': 'upload ', 'inputtype': 'file', 'name': 'files', 'multiple': True}),
                   }


class WorkerEditForm(forms.ModelForm):
    class Meta:
        model = ManagerBlank
        fields = (
            # 'files',
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
            'condition',
            'worker'
        )


class WorkerBlankForm(forms.ModelForm):
    class Meta:
        model = ManagerBlank
        fields = (
            'print',
            'design',
            'machine',
        )


class OrderSearchForm(forms.ModelForm):
    class Meta:
        model = ManagerBlank

        fields = ['id', 'title', 'client', 'author', 'status', 'condition', 'worker', 'order']

        widgets = {'deadline': forms.DateInput(attrs={'id': 'davaToday', 'type': 'date'})}


class ManagerBlankFilesForm(forms.ModelForm):
    class Meta:
        model = ManagerBlankFiles

        fields = ['order', 'files']

        widgets = {
                    'files': forms.ClearableFileInput(attrs={'class': 'upload ', 'inputtype': 'file', 'name': 'files', 'multiple': True}),
                   }
