from django.urls import path

from trains import views


app_name = 'trains'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.TrainListView.as_view(), name='home'),
    path('add/', views.TrainCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.TrainDetailView.as_view(), name='detail_train'),
    path('update/<int:pk>/', views.TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TrainDeleteView.as_view(), name='delete'),

]

