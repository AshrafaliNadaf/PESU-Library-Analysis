from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookir.forms import  bookirForm
from .models import loginmodel, bookirmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def bookir(request, a=0):
    if request.method == "GET":
        if a == 0:
            forms = bookirForm()
        else:
            user1 = bookirmodel.objects.get(pk=a)
            forms = bookirForm(instance=user1)
        return render(request, "bookir.html", {'forms': forms})
    else:
        if a == 0:
            forms = bookirForm(request.POST)
        else:
            user1 = bookirmodel.objects.get(pk=a)
            forms = bookirForm(request.POST, instance=user1)
        if forms.is_valid():
            userid = request.session['username']
            current_user = loginmodel.objects.get(id=userid)
            instance2 = forms.save(commit=False)
            instance2.username_id = current_user.id
            instance2.save()
            forms.save()
        return redirect('bookir_info')


def bookir_info(request):
    context = {'obj': bookirmodel.objects.all()}
    return render(request, "bookir_info.html", context)


def bookir_delete(request, a):
    user = bookirmodel.objects.get(pk=a)
    user.delete()
    return redirect('bookir_info')
