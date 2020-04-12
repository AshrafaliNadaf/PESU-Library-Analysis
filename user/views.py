from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import RegisterForms,VisitorForms,newbookForm,bookirForm
from .models import loginmodel, visitorsmodel, bookirmodel, newbookmodel
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


# @login_required(login_url='login')
def register(request, id=0):
    if request.method == "GET":
        if id == 0:    
            forms = RegisterForms()
        else:
            user = loginmodel.objects.get(pk=id)
            forms = RegisterForms(instance=user)
        return render(request, "register.html",{'forms':forms})
    else:
        if id == 0:
            forms = RegisterForms(request.POST)
        else:
            user = loginmodel.objects.get(pk=id)
            forms = RegisterForms(request.POST,instance=user)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            forms.save()
            
        return redirect('profile')


# @login_required
def home(request):
    return render(request, 'dashboard.html')

#profile
def profile(request):
    context = {'profile_list': loginmodel.objects.all()}
    return render(request, "profile.html", context)

#book Request/return
def bookir(request):
    if request.method == "POST":
        forms = bookirForm(request.POST)
        if forms.is_valid():
           userid = request.session['username']
           current_user = loginmodel.objects.get(id=userid)
           instance = forms.save(commit=False)
           instance.username_id = current_user.id
           instance.save()
           return redirect('bookir_info')
    else:
        if request.method == "GET":
            # user =  bookirmodel.objects.get()
            forms = bookirForm()
            return render(request, "bookir.html", {'forms': forms})

def bookir_info(request):
    if request.method == "GET":
        context = {'obj': bookirmodel.objects.all()}
        return render(request, "bookir_info.html", context)


#Vistors
def visitors(request):
    if request.method == "POST":
        forms = VisitorForms(request.POST)
        if forms.is_valid():
           userid = request.session['username']
           current_user = loginmodel.objects.get(id=userid)
           instance = forms.save(commit=False)
           instance.username_id = current_user.id
           instance.save()
           return redirect('visitor_info')
    else:
        if request.method == "GET":
            # user =  bookirmodel.objects.get()
            forms = VisitorForms()
            return render(request, "visitors.html", {'forms': forms})

def visitor_info(request):
    if request.method == "GET":
        context = {'obj': visitorsmodel.objects.all()}
        return render(request, "visitor_info.html", context)
        

#New book
def newbook(request):
    if request.method == "GET":
        forms = newbookForm()
        return render(request, "newbook.html", {'forms': forms})
    else:
        forms = newbookForm(request.POST)
        if forms.is_valid():
            userid = request.session['username']
            current_user = loginmodel.objects.get(id=userid)
            instance = forms.save(commit=False)
            instance.username_id = current_user.id
            instance.save()
        return redirect('newbook')

def mydetails(request):
    ()


def update_details(request):
    ()
