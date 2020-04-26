from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookir.forms import  bookirForm
from .models import loginmodel, bookirmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def bookir(request, a=0,d=0):
    user = request.session['username']
    type = loginmodel.objects.get(id=user)
    if d==0:
        if request.method == "GET":
            if a == 0:
                forms = bookirForm()
            else:
                user1 = bookirmodel.objects.get(pk=a)
                forms = bookirForm(instance=user1)
            return render(request, "bookir.html", {'forms': forms,'type': type})
        else:
            if a == 0:
                forms = bookirForm(request.POST)
            else:
                user1 = bookirmodel.objects.get(pk=a)
                forms = bookirForm(request.POST, instance=user1)
            if forms.is_valid():
                messages.success(request, f'Data Updated.')
                userid = request.session['username']
                current_user = loginmodel.objects.get(id=userid)
                instance2 = forms.save(commit=False)
                instance2.username_id = current_user.id
                instance2.save()
                forms.save()
            return redirect('bookir_info')
    else:
        messages.warning(request,'Data Deleted.')
        bookirmodel.objects.filter(pk=a).delete()
        return redirect('bookir_info')


def bookir_info(request):
    user = request.session['username']
    type = loginmodel.objects.get(id=user)
    obj= bookirmodel.objects.all()
    return render(request, "bookir_info.html",{'obj':obj,'type':type})

