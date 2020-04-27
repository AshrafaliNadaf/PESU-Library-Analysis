from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookir.forms import  bookirForm
from .models import User, Bookir
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def bookir(request, a=0,d=0):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if d==0:
        if request.method == "GET":
            if a == 0:
                forms = bookirForm()
            else:
                user2 = Bookir.objects.get(pk=a)
                forms = bookirForm(instance=user2)
            return render(request, "bookir.html", {'forms': forms,'type': type})
        else:
            if a == 0:
                forms = bookirForm(request.POST)
            else:
                user2 = Bookir.objects.get(pk=a)
                forms = bookirForm(request.POST, instance=user2)
            if forms.is_valid():
                messages.success(request, f'Data Updated.')
                userid = request.session['username']
                current_user = User.objects.get(id=userid)
                instance2 = forms.save(commit=False)
                if current_user.usertype == "user":
                    instance2.user_id = current_user.id
                else:
                    user2 = Bookir.objects.get(pk=a)
                    instance2.user_id = user2.id
                instance2.save()
                forms.save()
            return redirect('bookir_info')
    else:
        messages.warning(request,'Data Deleted.')
        Bookir.objects.filter(pk=a).delete()
        return redirect('bookir_info')


def bookir_info(request):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if type.usertype=="user":
        obj= Bookir.objects.filter(user=type.id)
    else:
        obj = Bookir.objects.all()
    return render(request, "bookir_info.html",{'obj':obj,'type':type})

