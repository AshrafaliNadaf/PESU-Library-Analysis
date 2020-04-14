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
            form = RegisterForms(instance=user)
        return render(request, "register.html",{'form':form})
    else:
        if id == 0:
            form = RegisterForms(request.POST)
        else:
            user = loginmodel.objects.get(pk=id)
            form = RegisterForms(request.POST,instance=user)
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
def bookir(request, a=0):
    if request.method == "GET":
        if a == 0:
            forms = bookirForm()
        else:
            user1 = bookirmodel.objects.get(pk=a)
            forms = bookirForm(instance=user1)
        return render(request, "bookir.html", {'forms': forms})
    else:
        if a == 0:
            forms = bookirForm(request.POST)
        else:
            user1 = bookirmodel.objects.get(pk=a)
            forms = bookirForm(request.POST, instance=user1)
        if forms.is_valid():
            userid = request.session['username']
            current_user = loginmodel.objects.get(id=userid)
            instance2 = forms.save(commit=False)
            instance2.username_id = current_user.id
            instance2.save()
            forms.save()
        return redirect('bookir_info')
        

def bookir_info(request):
    context = {'obj': bookirmodel.objects.all()}
    return render(request, "bookir_info.html", context)

def bookir_delete(request,a):
    user = bookirmodel.objects.get(pk=a)
    user.delete()
    return redirect('bookir_info')


#Vistors
def visitors(request, id=0):
    if request.method == "GET":
        if id == 0:
            forms = VisitorForms()
        else:
            user = visitorsmodel.objects.get(pk=id)
            forms = VisitorForms(instance=user)
        return render(request, "visitors.html", {'forms': forms})
    else:
        if id == 0:
            forms = VisitorForms(request.POST)
        else:
            user = visitorsmodel.objects.get(pk=id)
            forms = VisitorForms(request.POST, instance=user)
        if forms.is_valid():
            userid = request.session['username']
            current_user = loginmodel.objects.get(id=userid)
            instance1 = forms.save(commit=False)
            instance1.username_id = current_user.id
            instance1.save()
            forms.save()
        return redirect('visitor_info')

def visitor_info(request):
    context = {'obj': visitorsmodel.objects.all()}
    return render(request, "visitor_info.html", context)


# def visitors_delete(request, id):
#     user = visitorsmodel.objects.get(pk=id)
#     user.delete()
#     return redirect('visitor_info')

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
