from django import forms
from django.core.exceptions import ValidationError

from orders.models import ManagerBlank


class ManagerBlankForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['condition'].empty_label = "Не начато"
        self.fields['worker'].empty_label = "Не выбран"
        self.fields['order'].empty_label = "Не выбрано"
        self.fields['client'].empty_label = "Не выбран"

    class Meta:
        model = ManagerBlank
        fields = (
            'files',
            'title',
            'description',
            'deadline',
            'client',
            # 'status',
            'price',
            'order',
            'condition',
            'worker',
        )
        widgets = {'deadline': forms.DateInput(attrs={'id': 'davaToday', 'type': 'date'})}

    # def clean_client(self):
    #     client = self.cleaned_data['client']
    #
    #     if str(client) == None:
    #         raise ValidationError('Вы не выбрали клиента')
    #     return client


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


class OrderSearchForm(forms.ModelForm):
    class Meta:
        model = ManagerBlank

        fields = ['id', 'title', 'client', 'author', 'status', 'condition', 'worker', 'order']

        widgets = {'deadline': forms.DateInput(attrs={'id': 'davaToday', 'type': 'date'})}
