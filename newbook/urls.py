from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('newbook/', views.newbook, name='newbook'),
    path('newbook_info/', views.newbook_info, name='newbook_info')
]
