# from django.contrib import admin
from django.urls import path, include

from routes import views

urlpatterns = [
    # path('salom/', admin.site.urls),
    path('', views.home, name='home'),
    path('find_routes/', views.find_routes, name='find_routes'),
    path('add_route/', views.add_route, name='add_route'),
    path('save_route/', views.save_route, name='save_route'),
    path('list/', views.RouteListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.RouteDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.RouteDeleteView.as_view(), name='delete'),
    path('cities/', include('cities.urls', namespace='cities')),
    path('trains/', include('trains.urls', namespace='trains')),
    path('account/', include('account.urls', namespace='account')),
]
