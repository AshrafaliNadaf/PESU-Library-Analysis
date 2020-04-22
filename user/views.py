from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import newbookForm
from register.forms import RegisterForms
from .models import  newbookmodel 
from register.models import loginmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
# Create your views here.

def login(request):
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = loginmodel.objects.get(username=usid, password=pswd)
            request.session['username'] = check.id
            return redirect('home')
        except:
            pass
        messages.error(request,f'Invalid Username/Password')
    return render(request, 'login.html')

# @login_required
def home(request):
    user = request.session['username']
    type =  loginmodel.objects.get(id=user)
    return render(request, 'dashboard.html',{'type': type})

#profile
def profile(request):
    user = request.session['username']
    type = loginmodel.objects.get(id=user)
    if type.usertype=="admin" :
        context = {'profile_list': loginmodel.objects.all()}
        return render(request, "profile.html", context)
    return redirect('home')

#New book
def newbook(request):
    if request.method == "GET":
        user = request.session['username']
        type = loginmodel.objects.get(id=user)
        forms = newbookForm()
        return render(request, "newbook.html", {'forms': forms,'type':type})
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

def mydetails(request):
    ()

def update_details(request):
    ()
