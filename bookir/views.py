from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookir.forms import  bookirForm
from .models import Bookir
from register.models import extendedUser
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def bookir(request, a=0,d=0):
    #user1 = request.session['username']
    type1 = extendedUser.objects.get(user=request.user)
    if d==0:
        if request.method == "GET":
            if a == 0:
                forms = bookirForm()
            else:
                user2 = Bookir.objects.get(pk=a)
                forms = bookirForm(instance=user2)
            return render(request, "bookir.html", {'forms': forms,'type': type1})
        else:
            if a == 0:
                forms = bookirForm(request.POST)
            else:
                user2 = Bookir.objects.get(pk=a)
                forms = bookirForm(request.POST, instance=user2)
            if forms.is_valid():
                messages.success(request, f'Data Updated.')
                #userid = request.session['username']
                current_user = extendedUser.objects.get(user=request.user)
                instance2 = forms.save(commit=False)
                if current_user.usertype == "user":
                    instance2.user_id = current_user.id
                else:
                    user2 = Bookir.objects.get(pk=a)
                    instance2.user_id = user2.user_id
                instance2.save()
                forms.save()
            return redirect('bookir_info')
    else:
        messages.warning(request,'Data Deleted.')
        Bookir.objects.filter(pk=a).delete()
        return redirect('bookir_info')


@login_required(login_url='login')
def bookir_info(request):
    #user1 = request.session['username']
    type1 = extendedUser.objects.get(user=request.user)
    if type1.usertype=="user":
        obj= Bookir.objects.filter(user=type1.id)
    else:
        obj = Bookir.objects.all()
    return render(request, "bookir_info.html",{'obj':obj,'type':type1})

