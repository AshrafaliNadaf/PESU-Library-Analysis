from django import forms
from .models import User

class RegisterForms(forms.ModelForm):
    class Meta:
        model=User
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
    
