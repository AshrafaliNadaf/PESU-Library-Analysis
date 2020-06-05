from django.shortcuts import render, redirect
from django.http import HttpResponse
from register.forms import RegisterForms
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# @login_required(login_url='login')

def register(request, id=0,d=0):
    user1 = request.session['username']
    type = User.objects.get(id=user1)
    if d == 0:
        if request.method == "GET":
            if id == 0:
                forms = RegisterForms()
            else:
                user = User.objects.get(pk=id)
                forms = RegisterForms(instance=user)
            return render(request, "register.html", {'form': forms,'type':type})
        else:
            if id == 0:
                forms = RegisterForms(request.POST)
            else:
                user = User.objects.get(pk=id)
                forms = RegisterForms(request.POST, instance=user)
            if forms.is_valid():
                username = forms.cleaned_data.get('username')
                messages.success(request, f'Account of "{username}"  Updated.')
                forms.save()
            return redirect('profile')
    else:
        messages.warning(request, 'User Deleted.')
        User.objects.filter(pk=id).delete()
        return redirect('profile')
