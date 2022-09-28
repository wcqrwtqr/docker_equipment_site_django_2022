from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashHomePage.as_view(), name='dashboard'),
    path('query1/', views.DashboardQueryOne.as_view(), name='dashboardQuery'),
    path('querymain/', views.DashboardQueryMain.as_view(), name='dashboardQueryMain'),
]
