
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ExtRegiserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class EditBalForm(forms.Form):
    balance = forms.IntegerField(label='Сумма пополнения')