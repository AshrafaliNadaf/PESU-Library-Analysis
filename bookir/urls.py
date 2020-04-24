from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('<int:a><int:d>/', views.bookir, name='bookir_update'),
    # path('<int:a>/', views.bookir, name='bookir_delete'),
    path('bookir_info/', views.bookir_info, name='bookir_info'),
    path('bookir/', views.bookir, name='bookir'),
]
