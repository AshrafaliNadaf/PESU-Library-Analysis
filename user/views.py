from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import RegisterForms,VisitorForms,newbookForm, bookirForm
from .models import loginmodel, visitorsmodel, bookirmodel, newbookmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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


# def visitors(request):
#     if request.method == "GET":
#         forms = VisitorForms()
#         return render(request, "visitors.html",{'forms':forms})
        
#     else:
#         forms = VisitorForms(request.POST)
#         if forms.is_valid():
#             forms.save()
#         return redirect('visitors')

def visitors(request, id=0):
    if request.method == "GET":
        if id == 0:
            forms = VisitorForms()
        else:
            user = visitorsmodel.objects.get(pk=id)
            forms = VisitorForms(instance=user)
        # forms = VisitorForms()
        return render(request, "visitors.html", {'forms': forms})
    else:
        forms = VisitorForms(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('visitors')
        

# @login_required
def home(request):
    return render(request, 'dashboard.html')


def profile(request):
    context = {'profile_list':loginmodel.objects.all()}
    return render(request, "profile.html", context)


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


def bookir(request):
    if request.method == "GET":
            forms = bookirForm()
            return render(request, "bookir.html",{'forms':forms})   
    else:
        forms = bookirForm(request.POST)
        if forms.is_valid():
           userid = request.session['username']
           current_user = loginmodel.objects.get(id=userid)
           instance = forms.save(commit=False)
           instance.username_id = current_user.id
           instance.save()
        return redirect('bookir')  


def mydetails(request):
    ()


def update_details(request):
    ()
