from django import forms
from .models import  newbookmodel


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
