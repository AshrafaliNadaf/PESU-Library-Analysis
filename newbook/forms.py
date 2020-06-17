from django import forms
from .models import  Newbook

CHOICES = [('Student', 'Student'), ('Staff', 'Staff')]
class newbookForm(forms.ModelForm): 
    role = forms.ChoiceField(label='Requested by', widget=forms.RadioSelect(), choices=CHOICES)
    class Meta: 
        model = Newbook
        fields = ("authorname", "title", "publisher", "isbn",
                  "edition", "price", "copies", "role", "usn")
        labels = {
            'authorname': 'Author/s Name:',
            'isbn':"ISBN",
            'copies':'NO.Of Copies',
            'usn':'USN',
            'role':'Requested by'
        }
    def __init__(self, *args, **kwargs):
        super(newbookForm, self).__init__(*args, **kwargs)
        self.fields['price'].required = False
        self.fields['isbn'].required = False
        
