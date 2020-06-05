from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from bookir.models import Bookir
from register.models import User
from user.models import Department
from visitors.models import Visitor


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
    
#visitor chart
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

#visitors report
def visitor_rep(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    return render(request, "visitor_rep.html", {'type': type})

