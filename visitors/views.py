from django.shortcuts import render, redirect
from django.http import HttpResponse
from visitors.forms import VisitorForms
from .models import  Visitor,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def visitors(request, id=0,d=0):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if d == 0:
        if request.method == "GET":
            if id == 0:
                forms = VisitorForms()
            else:
                user1 = Visitor.objects.get(pk=id)
                forms = VisitorForms(instance=user1)
            return render(request, "visitors.html", {'forms': forms,'type':type})
        else:
            if id == 0:
                forms = VisitorForms(request.POST)
            else:
                user1 = Visitor.objects.get(pk=id)
                forms = VisitorForms(request.POST, instance=user1)
            if forms.is_valid():
                messages.success(request, f'Data Updated.')
                userid = request.session['username']
                current_user = User.objects.get(id=userid)
                instance1 = forms.save(commit=False)
                if current_user.usertype == "user":
                    instance1.user_id = current_user.id
                else:
                    user1 = Visitor.objects.get(pk=id)
                    instance1.user_id = user1.id
                instance1.save()
                forms.save()
            return redirect('visitor_info')
    else:
        messages.warning(request,'Data Deleted.')
        Visitor.objects.filter(pk=id).delete()
        return redirect('visitor_info')


def visitor_info(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if type.usertype=="user":
        obj= Visitor.objects.filter(user=type.id)
    else:
        obj = Visitor.objects.all()
    return render(request, "visitor_info.html", {'obj': obj, 'type': type})

