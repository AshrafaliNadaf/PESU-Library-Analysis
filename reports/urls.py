from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('report/', views.report, name='report'),
    path('bookirrep/', views.bookirrep, name='bookirrep'),
    path('bookir_chart/', views.bookir_chart, name='bookir_chart'),
    path('bookir_chart1/', views.bookir_chart1, name='bookir_chart1'),
    path('bookir_chart2/', views.bookir_chart2, name='bookir_chart2'),
    path('visitor_rep/', views.visitor_rep, name='visitor_rep'),
    path('visitor_chart/', views.visitor_chart, name='visitor_chart'),


]
