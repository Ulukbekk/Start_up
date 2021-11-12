from django import forms
from orders.models import ManagerBlank


class ManagerBlankForm(forms.ModelForm):
    class Meta:
        model = ManagerBlank
        fields = (
            'files',
            'title',
            'description',
            'deadline',
            'client',
            'status',
            'price',
            'order',
            'condition',
            'worker',
        )


class WorkerEditForm(forms.ModelForm):
    class Meta:
        model = ManagerBlank
        fields = (
            'files',
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
