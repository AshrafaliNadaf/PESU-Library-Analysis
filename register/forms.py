from django import forms
from .models import loginmodel

class RegisterForms(forms.ModelForm):
    class Meta:
        model=loginmodel
        fields=("usertype","username","password","contactnum","email")
        labels = {
            'usertype': 'Type of User',
            'username': 'User Name',
            'contactnum': 'Contact Number',
            'email':'Email'
        }
    
    def __init__(self, *args, **kwargs):
        super(RegisterForms,self).__init__(*args, **kwargs)
        # self.fields['email'].required = False
    
