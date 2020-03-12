from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('<int:id>/', views.register, name='users_update'),
    path('newbook/', views.newbook, name='newbook'),
    path('visitors/', views.visitors, name='visitors'),
    path('bookir/',views.bookir,name="bookir"),
<<<<<<< HEAD
    path('visitors_list',views.visitors_list),
=======
>>>>>>> bf553a589dfdec5b5719e8df52dd7ff84761233b
]
