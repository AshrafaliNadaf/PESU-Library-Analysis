from django import forms
from user.models import loginmodel,visitorsmodel,bookirmodel

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
        super(RegisterForms, self).__init__(*args, **kwargs)
        # self.fields['department'].empty_label = "Select"
        # self.fields['contactnum'].required = False
        self.fields['email'].required=False
    
class VisitorForms(forms.ModelForm):
    class Meta:
        model=visitorsmodel
        fields=("students","staff","visitors")

class DateInput(forms.DateInput):
    input_type='date'

class bookirForm(forms.ModelForm):
    class Meta:
        model=bookirmodel
        date=forms.DateField(widget=DateInput)
        fields=("deptname","date","bookissue","bookreturn","bookrenew")
        
    
    def __init__(self,*args,**kwargs):
        super(bookirForm,self).__init__(*args,**kwargs)
        self.fields['deptname'].empty_label="Select Department"
        # self.fields['bookissue'].required=False
        # self.fields['bookreturn'].required=False
        # self.fields['bookrenew'].required=False
        
