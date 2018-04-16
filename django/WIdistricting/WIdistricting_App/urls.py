from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/get_districts/', views.get_districts, name='get_districts'),
    path('api/get_district_plans', views.get_district_plans, name='get_district_plans'),
    path('api/get_all_district_metrics', views.get_all_district_metrics, name='Get All District Metrics')
]
