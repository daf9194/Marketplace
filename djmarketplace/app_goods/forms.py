
from django import forms
from app_users.models import Profile

class AddGoodForm(forms.Form):
    quan = forms.IntegerField()

class ClearBasketForm(forms.Form):
    class Meta:
        model = Profile
        fields = ()