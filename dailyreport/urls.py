from django.urls import path
from . import views

urlpatterns = [
    path('dailyreport/<int:pk>', views.DailyreportDetailView.as_view(), name='dailyreport_detail'),
    path('', views.DailyReportListView.as_view(), name='dailyreport'),
    path('dailyreport/new/', views.DailyreportCreate.as_view(), name='dailyreport_new'),
    path('dailyreport/<int:pk>/update/', views.DailyreportUpdateView.as_view(), name='dailyreport_update'),
    path('equipment/<int:pk>/delete/', views.DailyreportDeleteView.as_view(), name='dailyreport_delete'),
]
