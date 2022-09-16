from django.urls import path
from . import views

urlpatterns = [
    path('equipment/<int:pk>', views.EquipmentDetailView.as_view(),
         name='equipment_detail'),
    path('', views.EquipmentListView.as_view(), name='equipment'),
    path('equipment/new/', views.EquipmentCreateView.as_view(),
         name='equipment_new'),
    path('equipment/<int:pk>/update/', views.EquipmentUpdateView.as_view(),
         name='equipment_update'),
    path('equipment/<int:pk>/delete/', views.EquipmentDeleteView.as_view(),
         name='equipment_delete'),
    # path('pdf/<int:pk>', views.equipment_render_pdf_view,
    # name='equipment_pdf'),
    # path('equipment/maintenace/', views.EquipmentMaintenanceListView.as_view(), name='equipment_maintenance_detail'),
]
