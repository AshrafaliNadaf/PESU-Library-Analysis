from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from bookir.models import Bookir
from register.models import User
from user.models import Department
from visitors.models import Visitor
from newbook.models import Newbook

#main report
def report(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    return render(request, "report.html", {'type': type})

#bookIR report 
def bookirrep(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if request.method == 'GET':
        return render(request, "bookirrep.html", {'type': type})

#chart
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

#chart1
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

#chart2
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

#visitors report
def visitor_rep(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    return render(request, "visitor_rep.html", {'type': type})

#visitor chart
def visitor_chart(request):
    labels=["Student","staff","visitor"]
    data=[]
    dept1=Visitor.objects.values('students').aggregate(Sum('students'))
    dept2=Visitor.objects.values('staff').aggregate(Sum('staff'))
    dept3=Visitor.objects.values('visitors').aggregate(Sum('visitors'))
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


<<<<<<< HEAD
=======

>>>>>>> 8dcee5e839c7579184471b5a737989feb40c90b6
#newbook report
def newbookrep(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    return render(request, "newbookrep.html", {'type': type})

#newbook chart
def newbookchart(request):
    labels=['Student','staff']
    data=[]

    student=Newbook.objects.filter(role="Student").aggregate(Sum('copies'))
    staff=Newbook.objects.filter(role="Staff").aggregate(Sum('copies'))
   
    for x,y in student.items():
         data.append(y)
    for x,z in staff.items():
         data.append(z)


    data={
        'labels':labels,
        'data':data
    }
    return JsonResponse(data)




