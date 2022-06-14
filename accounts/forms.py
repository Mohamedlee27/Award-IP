from django import forms
from .models import Account,UserProfile


class RegistrationForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'