from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import  login_required
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


# from docker_equipment_site_django_2022.dailyreport.filters import DailyreportFilter
from .filters import DailyreportFilter

from .forms import DailyForm
from . import models
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class DailyReportListView(ListView):
    template_name = 'dailyreport/dailyreport_page.html'
    # queryset = models.DailyreportDB.objects.all()
    model = models.DailyreportDB # new
    form_class = DailyForm
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['daily_filter'] = DailyreportFilter(self.request.GET, queryset=self.queryset)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        filter_dailyreport = DailyreportFilter(self.request.GET, queryset=qs)
        return filter_dailyreport.qs



class DailyreportCreate(SuccessMessageMixin, CreateView ):
    template_name = 'dailyreport/dailyreport_new.html'
    form_class = DailyForm
    model = models.DailyreportDB
    success_message = "%(jobid)s was crated successfully"
    success_url = reverse_lazy('dailyreport')

    def from_valid(self, form):
        self.object = form.save(commit = True)
        self.object = save()
        return super().form_valid(form)



class DailyreportDetailView(DetailView):
    template_name = 'dailyreport/dailyreport_detail.html'
    queryset = models.DailyreportDB.objects.all()
    context_object_name = 'dailyreport_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DailyreportUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'dailyreport/dailyreport_update.html'
    model = models.DailyreportDB
    success_url = reverse_lazy('dailyreport')
    success_message = "%(jobid)s was updated successfully"
    # form_class = DailyForm
    fields = "__all__" # when adding the form_class then no need for this line

class DailyreportDeleteView(PermissionRequiredMixin,SuccessMessageMixin,  DeleteView):
    permission_required = ("is_superuser", )
    model = models.DailyreportDB
    success_url = reverse_lazy('dailyreport')
    success_message = "Daily report record was deleted"
    template_name = 'dailyreport/dailyreport_confirm_delete.html'
