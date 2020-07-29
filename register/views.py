from django.shortcuts import render, redirect
from django.http import HttpResponse
from register.forms import RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth
from .models import extendedUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# @login_required(login_url='login')
@login_required(login_url='login')
def register(request, id=0,d=0):
    #user1 = request.session['username']
    type = extendedUser.objects.get(user=request.user)
    if d == 0:
        if request.method == "GET":
            if id == 0:
                forms = RegisterForms()
            else:
                user = User.objects.get(pk=id)
                forms = RegisterForms(instance=user)
                type2 = extendedUser.objects.get(user=user)
                context = {'form': forms, 'type': type, 'type2': type2}
            return render(request, "register.html", context)
        else:
            if id == 0:
                forms = RegisterForms(request.POST)
            else:
                user = User.objects.get(pk=id)
                extendedUser.objects.filter(user=request.user)
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
