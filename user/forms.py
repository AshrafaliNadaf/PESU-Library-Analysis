from django import forms
from user.models import loginmodel, visitorsmodel, bookirmodel, newbookmodel

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
        labels = {
            'date': DateInput(),
            'deptname': 'Department',
            'bookissue': 'No.Of Book Issue',
            'bookreturn': "No.Of Book Return",
            'bookrenew': 'No.Of Book Renew'
        }
          
    def __init__(self,*args,**kwargs):
        super(bookirForm,self).__init__(*args,**kwargs)
        self.fields['deptname'].empty_label="Select Department"
        

class newbookForm(forms.ModelForm):
    class Meta:
        model = newbookmodel
        fields = ("authorname", "title", "publisher","isbn", "edition", "price","copies")
        labels = {
            'authorname': 'Author/s Name:',
            'isbn':"ISBN",
            'copies':'NO.Of Copies'
        }
    def __init__(self, *args, **kwargs):
        super(newbookForm, self).__init__(*args, **kwargs)
        self.fields['price'].required = False
