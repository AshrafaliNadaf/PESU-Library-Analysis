from django.shortcuts import render, redirect
from django.http import HttpResponse
from newbook.forms import newbookForm
from register.forms import RegisterForms
from .models import newbookmodel
from register.models import loginmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def newbook(request):
    if request.method == "GET":
        user = request.session['username']
        type = loginmodel.objects.get(id=user)
        forms = newbookForm()
        return render(request, "newbook.html", {'forms': forms, 'type': type})
    else:
        forms = newbookForm(request.POST)
        if forms.is_valid():
            bookname = forms.cleaned_data.get('title')
            messages.success(request, f'New Book "{bookname}" Requested.')
            user = request.session['username']
            current_user = loginmodel.objects.get(id=user)
            instance = forms.save(commit=False)
            instance.username_id = current_user.id
            instance.save()
        return redirect('newbook')


def newbook_info(request):
    user = request.session['username']
    type = loginmodel.objects.get(id=user)
    obj = newbookmodel.objects.all()
    return render(request, "newbook_info.html", {'obj': obj, 'type': type})
