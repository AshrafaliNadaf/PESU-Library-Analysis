from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from register.forms import RegisterForms 
from register.models import User
from newbook.models import Newbook
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from  bookir.models import Bookir
from user.models import Department
from visitors.models import Visitor
# django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
# Create your views here.

def login(request):
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = User.objects.get(username=usid, password=pswd)
            request.session['username'] = check.id
            return redirect('home')
        except:
            pass
        messages.error(request,f'Invalid Username/Password')
    return render(request, 'login.html')

# @login_required
def home(request):
    user1 = request.session['username']
    type =  User.objects.get(id=user1)
    obj = Newbook.objects.all()
    return render(request, 'dashboard.html',{'type': type,'obj':obj})

#profile
def profile(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if type.usertype=="admin" :
        profile_list= User.objects.all()
        return render(request, "profile.html", {'profile_list': profile_list,'type':type})
    return redirect('home')


def devops(request):
    return render(request, 'devops.html')

def report(request):
        return  render(request,"report.html")

def bookirrep(request):
    if request.method=='GET':
        return render(request,"bookirrep.html")

def bookir_chart(request):
    labels=[]
    data=[]
    qury=Department.objects.values("deptname")
    dept2=Bookir.objects.values('deptname_id').annotate(Sum('bookissue'))
    for entry in dept2:
        data.append(entry['bookissue__sum'])
    for val in qury:
      labels.append(val['deptname'])
    data={
       'labels':labels,
       'data':data
    }
    return JsonResponse(data)

def bookir_chart1(request):
    labels=[]
    data=[]
    qury=Department.objects.values("deptname")
    dept1=Bookir.objects.values('deptname_id').annotate(Sum('bookreturn'))
    for entry in dept1:
        data.append(entry['bookreturn__sum'])
    for val in qury:
      labels.append(val['deptname'])
    data={
       'labels':labels,
       'data':data
    }
    return JsonResponse(data)

def bookir_chart2(request):
    labels=[]
    data=[]
   
    qury=Department.objects.values("deptname")
    dept=Bookir.objects.values('deptname_id').annotate(Sum('bookrenew'))
    
    for entry in dept:
        data.append(entry['bookrenew__sum'])
    for val in qury:
      labels.append(val['deptname'])
    data={
       'labels':labels,
       'data':data
    }
    return JsonResponse(data)
    
def visitor_rep(request):
    return render(request,"visitor_rep.html")


def visitor_chart(request):
    labels=["Student","staff","visitor"]
    data=[]
   
    
    dept1=Visitor.objects.values('students').annotate(Sum('students'))
    dept2=Visitor.objects.values('staff').annotate(Sum('staff'))
    dept3=Visitor.objects.values('visitors').annotate(Sum('visitors'))
    print(dept1)
    print(dept2)
    for entry in dept1:
        data.append(entry['students__sum'])
    for entry in dept2:
        data.append(entry['staff__sum'])
    for entry in dept3:
        data.append(entry['visitors__sum'])
    data={
       'labels':labels,
       'data':data
    }
    return JsonResponse(data)


def mydetails(request):
    ()

def update_details(request):
    ()
