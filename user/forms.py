from django import forms
from user.models import loginmodel

class RegisterForms(forms.ModelForm):
    class Meta:
        model=loginmodel
        fields=("usertype","username","password","contactnum","email")