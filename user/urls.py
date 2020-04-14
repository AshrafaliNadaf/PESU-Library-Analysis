from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('<int:a>/', views.bookir, name='bookir_update'),
    path('delete/<int:a>/', views.bookir, name='bookir_delete'),
    path('<int:id>/', views.register, name='users_update'),
    path('<int:id>/', views.visitors, name='visitors_update'),
    # path('delete/<int:id>/', views.visitors, name='visitors_delete'),
    path('newbook/', views.newbook, name='newbook'),
    path('visitors/', views.visitors, name='visitors'),
    path('bookir/',views.bookir, name='bookir'),
    path('bookir_info/', views.bookir_info, name='bookir_info'),
    path('visitor_info/', views.visitor_info, name='visitor_info')
]
