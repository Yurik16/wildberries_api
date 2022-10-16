from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/<int:pk>/', views.apiSingleRequest, name='api'),
    path('api/file/', views.apiReqFromFile, name='api_file'),
]
