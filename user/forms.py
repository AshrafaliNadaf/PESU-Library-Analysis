from django import forms
from user.models import loginmodel,visitors

class RegisterForms(forms.ModelForm):
    class Meta:
        model=loginmodel
<<<<<<< HEAD
        fields=("usertype","username","password","contactnum","email")
        
        
class VisitorForms(forms.ModelForm):
    class Meta:
        model=visitors
        fields=("students","staff","visitors")
        
    
    
=======
        fields = ("usertype", "username", "password", "contactnum", "email")
        labels = {
            'usertype': 'Type of User',
            'username': 'User Name',
            'contactnum': 'Contact Number',
            'email':'Email'
        }
    def __init__(self, *args, **kwargs):
        super(RegisterForms, self).__init__(*args, **kwargs)
        # self.fields['department'].empty_label = "Select"
        # self.fields['contactnum'].required = False
        self.fields['email'].required=False
>>>>>>> bf553a589dfdec5b5719e8df52dd7ff84761233b
