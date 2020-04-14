from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('profile/', views.profile, name = 'profile'),
    path('<int:a>/', views.bookir, name='bookir_update'),
    path('delete/<int:a>/', views.bookir, name='bookir_delete'),
    path('<int:id>/', views.register, name='users_update'),   
    path('<int:id>/', views.visitors, name='visitors_update'),
    # path('delete/<int:id>/', views.visitors, name='visitors_delete'),
    path('newbook/', views.newbook, name='newbook'),
    path('visitors/', views.visitors, name='visitors'),
    path('bookir',views.bookir, name='bookir'),
    path('bookir_info/', views.bookir_info, name='bookir_info'),
    path('visitor_info/', views.visitor_info, name='visitor_info')
]
