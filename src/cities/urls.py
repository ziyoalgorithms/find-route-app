from django.urls import path

from cities import views


app_name = 'cities'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='detail_city'),

]

