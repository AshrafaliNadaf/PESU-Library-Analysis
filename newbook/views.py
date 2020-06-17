from django.shortcuts import render, redirect
from django.http import HttpResponse
from newbook.forms import newbookForm
from register.forms import RegisterForms
from .models import Newbook
from register.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def newbook(request):
    if request.method == "GET":
        user1 = request.session['username']
        type = User.objects.get(id=user1)
        forms = newbookForm()
        return render(request, "newbook.html", {'forms': forms, 'type': type})
    else:
        forms = newbookForm(request.POST)
        if forms.is_valid():
            bookname = forms.cleaned_data.get('title')
            messages.success(request, f'New Book "{bookname}" Requested.')
            user1 = request.session['username']
            current_user = User.objects.get(id=user1)
            instance = forms.save(commit=False)
            instance.user_id = current_user.id
            instance.save()
        return redirect('newbook')


def newbook_info(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    obj = Newbook.objects.all()
    return render(request, "newbook_info.html", {'obj': obj, 'type': type})


def newbook_update(request,id=0,x=0):
    bookname = Newbook.objects.get(pk=id)
    if x == 0:
        Newbook.objects.filter(pk=id).update(status="Approved")
        Newbook.objects.filter(pk=id).update(ack=1)
        messages.success(request, f'Book " {bookname.title} " Approved.')
    elif x == 1:
        Newbook.objects.filter(pk=id).update(status="Rejected")
        Newbook.objects.filter(pk=id).update(ack=1)
        messages.warning(request, f'Book " {bookname.title} " Rejected.')
    return redirect('newbook_info')

