from django.shortcuts import render, redirect
from django.http import HttpResponse
from register.forms import RegisterForms
from .models import loginmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# @login_required(login_url='login')

def register(request, id=0):
    if request.method == "GET":
        if id == 0:
            forms = RegisterForms()
        else:
            user = loginmodel.objects.get(pk=id)
            forms = RegisterForms(instance=user)
        return render(request, "register.html", {'form': forms})
    else:
        if id == 0:
            forms = RegisterForms(request.POST)
        else:
            user = loginmodel.objects.get(pk=id)
            forms = RegisterForms(request.POST, instance=user)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            messages.success(request, f'Account of {username} Updated.')
            forms.save()
        return redirect('profile')
