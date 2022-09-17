# from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View, CreateView
from .models import MaintenanceDB
from django.urls import  reverse_lazy
from .forms import MaintenanceForm
from .filters import Maintenancefilter
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

class MaintenanceHomePage(ListView):
    template_name = 'equipmenMaintenance/maintenance_page.html'
    queryset = MaintenanceDB.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Maintenancefilter(self.request.GET, queryset=self.queryset)
        return context

class MaintenanceDetailView(DetailView):
    queryset = MaintenanceDB.objects.all()
    template_name = 'equipmenMaintenance/maintenance_detail.html'
    context_object_name = 'maintenance_detail'

class MaintenanceCreate(CreateView ):
    template_name = 'equipmenMaintenance/maintenance_new.html'
    form_class = MaintenanceForm
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)

class MaintenanceDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = ("is_superuser", )
    template_name = 'equipmenMaintenance/maintenance_confirm_delete.html'
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')

class MaintenanceUpdateView(UpdateView):
    template_name = 'equipmenMaintenance/maintenance_update.html'
    model = MaintenanceDB
    success_url = reverse_lazy('maintenance')
    fields = "__all__"
