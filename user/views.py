from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import RegisterForms
from .models import loginmodel
#m django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
# Create your views here.

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
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        forms = RegisterForms(request.POST)
        print("posted")
        if forms.is_valid():
            print("validated")
            forms.save()
            return redirect('register')
    else:
        forms = RegisterForms()
        print("else")
    return render(request, "register.html",{'forms':forms})

def visitors(request):
    return render(request,'visitors.html')


def home(request):
    return render(request, 'dashboard.html')


def profile(request):
    return render(request, 'profile.html')


def newbook(request):
    return render(request, 'newbook.html')

def bookir(request):
        return render(request,'bookir.html')


def mydetails(request):
    ()


def update_details(request):
    ()
