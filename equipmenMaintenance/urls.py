from django.urls import path
from . import views

urlpatterns = [
    path('', views.MaintenanceHomePage.as_view(), name='maintenance'),
    path('maintenance/<int:pk>', views.MaintenanceDetailView.as_view(), name='maintenance_detail'),
    path('maintenance/<int:pk>/delete', views.MaintenanceDeleteView.as_view(), name='maintenance_delete'),
    path('maintenance/<int:pk>/update', views.MaintenanceUpdateView.as_view(), name='maintenance_update'),
    path('maintenance/new/', views.MaintenanceCreate.as_view(), name='maintenance_new'),
    # path('pdf/<int:pk>', views.maintenance_render_pdf_view, name='pdf_maintenance_view'),
]
