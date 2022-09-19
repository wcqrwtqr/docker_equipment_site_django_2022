from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import  login_required
from django.urls import reverse_lazy
from django import forms
from .forms import EquipmentForm
from . import models
from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import Q
# from equipmentMaintenance.models import MaintenanceDB
# from .filters import EquipmentFilter, EquipmentMaintenanceFilter
from .filters import EquipmentFilter
# from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa


class EquipmentListView(ListView):

    template_name = 'equipmentList/equipment_page.html'
    # queryset = models.EQUIPMENT_DB.objects.all()
    model = models.EQUIPMENT_DB # new
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EquipmentFilter(self.request.GET, queryset=self.queryset)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        filter_equipment = EquipmentFilter(self.request.GET, queryset=qs)
        return filter_equipment.qs

# # Getting the equipment vs maintenance views and filtering them
# class EquipmentMaintenanceListView(ListView):
#     template_name = 'equipmentList/equipment_maintenance_detail.html'
#     queryset = MaintenanceDB.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = EquipmentMaintenanceFilter(self.request.GET, queryset=self.queryset)
#         return context

class EquipmentDetailView(DetailView):
    template_name = 'equipmentList/equipment_detail.html'
    queryset = models.EQUIPMENT_DB.objects.all()
    context_object_name = 'equipment_detail'


class EquipmentCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("is_superuser")
    template_name = 'equipmentList/equipment_new.html'
    form_class = EquipmentForm
    model = models.EQUIPMENT_DB
    success_url = reverse_lazy('equipment')

    def from_valid(self,form):
        '''
        Validate the form before saving
        '''
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)


class EquipmentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ("is_superuser", )
    model = models.EQUIPMENT_DB
    success_url = reverse_lazy('equipment')
    template_name = 'equipmentList/equipment_confirm_delete.html'


class EquipmentUpdateView(UpdateView):
    model = models.EQUIPMENT_DB
    fields = '__all__'
    template_name = 'equipmentList/equipment_update.html'
    success_url = reverse_lazy('equipment')

