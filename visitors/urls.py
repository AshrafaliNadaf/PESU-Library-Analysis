from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<int:id>/', views.visitors, name='visitors_update'),
    path('delete/<int:id>/', views.visitors, name='visitors_delete'),
    path('visitors/', views.visitors, name='visitors'),
    path('visitor_info/', views.visitor_info, name='visitor_info')
]
