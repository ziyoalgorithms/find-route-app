from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('salom/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cities/', include('cities.urls', namespace='cities')),
    path('trains/', include('trains.urls', namespace='trains'))
]
