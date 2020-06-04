from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from  bookir.models import Bookir
from user.models import Department
from visitors.models import Visitor
from newbook.models import Newbook
# django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
# Create your views here.



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
    dept1=Visitor.objects.values('students').aggregate(Sum('students'))
    dept2=Visitor.objects.values('staff').aggregate(Sum('staff'))
    dept3=Visitor.objects.values('visitors').aggregate(Sum('visitors'))
    print(dept1)
    print(dept2)
    print(dept3)
    for x,y in dept1.items():
        data.append(y)
    for x,z in dept2.items():
        data.append(z)
    for x,w in dept3.items():
        data.append(w)
    data={
       'labels':labels,
       'data':data
    }
    return JsonResponse(data)

def newbookrep(request):
    return render(request,"newbookrep.html")

def newbookchart(request):
    labels=['Student','staff']
    data=[]

    student=Newbook.objects.filter(role="Student").aggregate(Sum('copies'))
    staff=Newbook.objects.filter(role="Staff").aggregate(Sum('copies'))
    print(student)
    print(staff)
    for x,y in student.items():
         data.append(y)
    for x,z in staff.items():
         data.append(z)


    data={
        'labels':labels,
        'data':data
    }
    return JsonResponse(data)




def ack_update(request, z=0):
    Newbook.objects.filter(pk=z).update(ack=0)
    return redirect('home')


def mydetails(request):
    ()

def update_details(request):
    ()

# Create your views here.
