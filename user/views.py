from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from user.forms import RegisterForms,VisitorForms,bookirForm
from .models import loginmodel,visitorsmodel,bookirmodel
=======
from user.forms import RegisterForms,VisitorForms,newbookForm
from .models import loginmodel, visitorsmodel, bookirmodel, newbookmodel
>>>>>>> e38730e7c75595e80cb6d0f4d51102692804198a
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
            forms.save()
        return redirect('profile')



def visitors(request):
    if request.method == "GET":
        forms = VisitorForms()
        return render(request, "visitors.html",{'forms':forms})
        
    else:
        
        forms = VisitorForms(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('visitors')
        

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
            current_user = loginmodel.objects.get('usertype')
            instance = forms.save(commit=False)
            instance.usertype = current_users
            instance.save()
        return redirect('newbook')

def bookir(request):
    if request.method == "GET":
            print("entered if")
            forms = bookirForm()
            return render(request, "bookir.html",{'forms':forms})
        
    else:
        print("entered else")
        forms = bookirForm(request.POST)
        if forms.is_valid():
                forms.save()
        return redirect('bookir')  

        


def mydetails(request):
    ()

def update_details(request):
    ()
