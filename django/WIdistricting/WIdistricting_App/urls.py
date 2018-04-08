from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('API_get_districts/', views.get_districts, name='get_districts'),
]
