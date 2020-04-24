from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('register/', views.register, name='register'),
    path('<int:id><int:d>/', views.register, name='users_update'),
]
