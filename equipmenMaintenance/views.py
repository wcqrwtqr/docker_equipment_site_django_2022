# from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View, CreateView
from .models import MaintenanceDB
from django.urls import  reverse_lazy
from .forms import MaintenanceForm
from .filters import Maintenancefilter
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib import messages
# Create your views here.

# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

class MaintenanceHomePage(ListView):
    template_name = 'equipmenMaintenance/maintenance_page.html'
    # queryset = MaintenanceDB.objects.all()
    model = MaintenanceDB
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Maintenancefilter(self.request.GET, queryset=self.queryset)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        filter_maintenance = Maintenancefilter(self.request.GET, queryset=qs)
        return filter_maintenance.qs

class MaintenanceDetailView(DetailView):
    queryset = MaintenanceDB.objects.all()
    template_name = 'equipmenMaintenance/maintenance_detail.html'
    context_object_name = 'maintenance_detail'

class MaintenanceCreate(SuccessMessageMixin,CreateView ):
    template_name = 'equipmenMaintenance/maintenance_new.html'
    form_class = MaintenanceForm
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')
    success_message = "%(ms_type)s was created successfully"

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        # success_message = "Maintenance created"
        return super().form_valid(form)

class MaintenanceDeleteView(SuccessMessageMixin,PermissionRequiredMixin,DeleteView):
    permission_required = ("is_superuser", )
    template_name = 'equipmenMaintenance/maintenance_confirm_delete.html'
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')
    success_message = "Main record was deleted"

# class MaintenanceUpdateView(SuccessMessageMixin,UpdateView):
class MaintenanceUpdateView(SuccessMessageMixin,UpdateView):
    model = MaintenanceDB
    fields = "__all__"
    success_url = reverse_lazy('maintenance')
    template_name = 'equipmenMaintenance/maintenance_update.html'
    # success_message = "Maintenance updated"
    success_message = "%(asset)s was updated successfully"
