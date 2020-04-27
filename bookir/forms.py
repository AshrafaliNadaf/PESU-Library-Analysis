from django import forms
from .models import Bookir


class DateInput(forms.DateInput):
    input_type='date'

class bookirForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=Bookir
        fields=("deptname","date","bookissue","bookreturn","bookrenew")
        labels = { 
            'deptname': '',
            'bookissue': 'NO.Of Books Issue',
            'bookreturn': "NO.Of Books Return",
            'bookrenew': 'NO.Of Books Renewed'
        }
          
    def __init__(self,*args,**kwargs):
        super(bookirForm,self).__init__(*args,**kwargs)
        self.fields['deptname'].empty_label="Select Department"
        
