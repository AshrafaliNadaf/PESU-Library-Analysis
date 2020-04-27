from django import forms
from .models import  Visitor


class DateInput(forms.DateInput):
    input_type='date'  

class VisitorForms(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Visitor
        fields = ("date", "students", "staff", "visitors")
        labels = {
            'students': 'NO.Of Students',
            'staff': "NO.Of Staffs",
            'visitors': "NO.Of Guests"
        }

