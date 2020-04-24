from django.shortcuts import render, redirect
from django.http import HttpResponse
from register.forms import RegisterForms 
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
        profile_list= loginmodel.objects.all()
        return render(request, "profile.html", {'profile_list': profile_list,'type':type})
    return redirect('home')

#New book


def mydetails(request):
    ()

def update_details(request):
    ()
