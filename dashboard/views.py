from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Avg, Max, Min, FloatField, Count, IntegerField, Sum
from equipmentList.models import EQUIPMENT_DB as db
from equipmenMaintenance.models import MaintenanceDB as dbm
import pandas as pd
# from equipmentList import models

class DashHomePage(TemplateView):
    template_name = 'dashboard/dashboard_page.html'

class DashboardQueryOne(ListView):
    template_name = 'dashboard/dashboard_page_query_1.html'
    context_object_name = 'dash_query1'

    def get_queryset(self):
        return db.objects.all().order_by('asset_num')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q1'] = db.objects.all().order_by('asset_num')[:10]
        # The bad way TODO, need to get a better action for querying over the data
        context['qs_av_KIUSLS'] = db.objects.filter(BL='SLS', BU='KIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
        context['qs_av_KIUSWT'] = db.objects.filter(BL='SWT', BU='KIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
        context['qs_av_SIUSLS'] = db.objects.filter(BL='SLS', BU='SIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
        context['qs_av_SIUSWT'] = db.objects.filter(BL='SWT', BU='SIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
        context['qs_av_SIUWHM'] = db.objects.filter(BL='WHM', BU='SIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
        context['qs_av_SIUSLS'] = db.objects.filter(BL='SLS', BU='SIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
        context['qs_av_SIUSWT'] = db.objects.filter(BL='SWT', BU='SIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
        context['qs_av_SIUWHM'] = db.objects.filter(BL='WHM', BU='SIU').aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))

        return context


class DashboardQueryMain(ListView):
    template_name = 'dashboard/dashboard_page_query_main.html'
    context_object_name = 'dash_query_main'

    def get_queryset(self):
        return dbm.objects.all().order_by('main_date_start')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q1'] = dbm.objects.all().order_by('main_date_start')[:10]
        # The bad way TODO, need to get a better action for querying over the data
        context['MS_1'] = dbm.objects.filter(ms_type='MS-1').count()
        context['MS_2'] = dbm.objects.filter(ms_type='MS-2').count()
        context['MS_3'] = dbm.objects.filter(ms_type='MS-3').count()
        context['MS_4'] = dbm.objects.filter(ms_type='MS-4').count()
        context['Repair'] = dbm.objects.filter(ms_type='Repair').count()
        context['Down'] = dbm.objects.filter(ms_type='Down').count()
        context['Junked'] = dbm.objects.filter(ms_type='Junked').count()
        context['Waiting_on_Spares'] = dbm.objects.filter(ms_type='Waiting on Spares').count()

        return context
