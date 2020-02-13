from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import RegisterForms
from .models import loginmodel
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
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        forms = RegisterForms()
    return render(request, 'register.html')

# def login(request):
#     if request.method == "POST":
#         if request.method == "POST":
#             usid = request.POST.get('name')
#             pswd = request.POST.get('password')
#             if usid == 'admin' and pswd == 'admin':
#                 return redirect('user_page')
#     return render(request,'home.html')


def home(request):
    return render(request, 'dashboard.html')


def mydetails(request):
    ()


def update_details(request):
    ()
