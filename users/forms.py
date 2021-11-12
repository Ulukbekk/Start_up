from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account, Client


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = UserCreationForm.Meta.fields + ('first_name',
                                                 'last_name',
                                                 'email',
                                                 'phone',
                                                 'position')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name',
                  'last_name',
                  'organization',
                  'phone',
                  'org_phone',
                  'amount_orders',
                  'status',
                  )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone'
        ]

