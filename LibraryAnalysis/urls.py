from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from user import views
urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('register/',include('register.urls')),
    path('bookir/', include('bookir.urls')),
    path('user/', include('user.urls')),
    path('visitors/', include('visitors.urls')),
]
