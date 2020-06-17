from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from register.forms import RegisterForms
from register.models import User
from newbook.models import Newbook
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from bookir.models import Bookir
from user.models import Department
from visitors.models import Visitor


#login
def login(request):
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = User.objects.get(username=usid, password=pswd)
            request.session['username'] = check.id
            request.session.set_test_cookie()
            return redirect('home')
        except:
            pass
        messages.error(request,f'Invalid Username/Password')
    return render(request, 'login.html')


# Home
def home(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    obj = Newbook.objects.all()
    return render(request, 'dashboard.html', {'type': type, 'obj': obj})

#profile
def profile(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if type.usertype=="admin" :
        profile_list= User.objects.all()
        return render(request, "profile.html", {'profile_list': profile_list,'type':type})
    return redirect('home')

#about page
def devops(request):
    return render(request, 'devops.html')

#ack update
def ack_update(request, z=0):
    Newbook.objects.filter(pk=z).update(ack=0)
    return redirect('home')


# def logout(request):
#     try:
#         del request.session['username']
#     except KeyError:
#         pass
#     return redirect('login')

def mydetails(request):
    ()

def update_details(request):
    ()
