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


def newbook_update(request,id=0,x=0):
    bookname = newbookmodel.objects.get(pk=id)
    if x == 0:
        newbookmodel.objects.filter(pk=id).update(status="Approved")
        messages.success(request, f'Book " {bookname.title} " Approved.')
    elif x == 1:
        newbookmodel.objects.filter(pk=id).update(status="Rejected")
        messages.warning(request, f'Book " {bookname.title} " Rejected.')
    return redirect('newbook_info')
