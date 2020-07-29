from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from register.forms import RegisterForms
from register.models import extendedUser
from django.contrib.auth.models import User
from django.contrib import auth
from newbook.models import Newbook
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from bookir.models import Bookir
from user.models import Department
from visitors.models import Visitor
from django.db.models import Count
from django.db.models import Sum



#login
def login(request):
    if request.method == "POST":
        user = auth.authenticate(
           username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')   
        messages.error(request,f'Invalid Username/Password')
    return render(request, 'login.html')


# Home
@login_required(login_url='login')
def home(request):
    #user1 = request.session['username']
    type = extendedUser.objects.get(user=request.user)
    obj = Newbook.objects.all()
    visitorCount = Visitor.objects.all().aggregate(a=Sum('students') + Sum('staff') + Sum('visitors'))
    count = visitorCount.get('a')
    libNo = User.objects.all().count() - 1
    bookTrans = Bookir.objects.all().count()
    return render(request, 'dashboard.html', {'type': type, 'obj': obj, 'count':count, 'libNo':libNo, 'bookTrans':bookTrans})

#profile
@login_required(login_url='login')
def profile(request):
    #user1 = request.session['username']
    type = extendedUser.objects.get(user=request.user)
    if type.usertype=="admin" :
        profile_list = User.objects.all()
        profile_list2 = extendedUser.objects.all()
        context = {'profile_list': profile_list,
                   'profile_list2': profile_list2, 'type': type}
        return render(request, "profile.html", context)
    return redirect('home')

#about page

def devops(request):
    return render(request, 'devops.html')

#ack update
@login_required(login_url='login')
def ack_update(request, z=0):
    Newbook.objects.filter(pk=z).update(ack=0)
    return redirect('home')


def logout(request):
    auth.logout(request)
    return render(request,'login.html')


def mydetails(request):
    ()

def update_details(request):
    ()
