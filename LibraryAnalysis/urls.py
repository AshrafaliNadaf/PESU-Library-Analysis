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
    path('<int:id>/', views.register, name='users_update'),
    path('newbook/', views.newbook, name='newbook'),
    path('visitors/', views.visitors, name='visitors'),
    path('bookir',views.bookir,name="bookir"),
]
