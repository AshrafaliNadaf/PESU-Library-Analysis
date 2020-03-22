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
        # self.fields['department'].empty_label = "Select"
        # self.fields['contactnum'].required = False
        self.fields['email'].required=False
        
class VisitorForms(forms.ModelForm):
    class Meta:
        model=visitorsmodel
        fields=("students","staff","visitors")

# class bookirForm(forms.ModelForm):
#     class Meta:
#         model=bookirmodel
#         fields=("deptname","date","bookissue","bookreturn","bookrenew")


class newbookForm(forms.ModelForm):
    class Meta:
        model = newbookmodel
        fields = ("authorname", "title", "publisher","isbn", "edition", "price","copies")
        labels = {
            'authorname': 'Author/s Name',
            'title': 'Title',
            'publisher': 'Publisher',
            'isbn':"ISBN",
            'edition':'Edition',
            'price':'Price',
            'copies':'NO.Of Copies'
        }
    def __init__(self, *args, **kwargs):
        super(newbookForm, self).__init__(*args, **kwargs)
        # self.fields['department'].empty_label = "Select"
        # self.fields['contactnum'].required = False
        self.fields['price'].required = False
