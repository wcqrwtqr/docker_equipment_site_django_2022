from builtins import print
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Avg, Max, Min, FloatField, Count, IntegerField, Sum
from equipmentList.models import EQUIPMENT_DB as db
from equipmenMaintenance.models import MaintenanceDB as dbm
from jobs.models import JobsDB as dbj
from dailyreport.models import DailyreportDB as dbd
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

        distinct_bl = db.objects.all().values_list('BL', flat=True).distinct()
        distinct_bu = db.objects.all().values_list('BU', flat=True).distinct()
        # Removing all the dublicates distinct values and put them in a set
        mybl = set(distinct_bl)
        mybu = set(distinct_bu)
        # =========== Getting the avg cost for equipments =========================
        equipmenet_cost_avg_dict = {}
        for bar in mybu:
            for baz in mybl:
                text = bar + '_' + baz
                x = db.objects.filter(BL=baz, BU=bar).aggregate(av=Avg('acquisition_cost', output_field=IntegerField()))
                if x['av'] is None:
                    # If the value is None then skip this point and move to the next one
                    continue
                equipmenet_cost_avg_dict[text] = x
        context['all_equipment_blbu_avg'] = equipmenet_cost_avg_dict
        # =========== Getting the avg nbv for equipments =========================
        equipmenet_nbv_avg_dict = {}
        for bar in mybu:
            for baz in mybl:
                text = bar + '_' + baz
                x = db.objects.filter(BL=baz, BU=bar).aggregate(av=Avg('nbv', output_field=IntegerField()))
                if x['av'] is None:
                    # If the value is None then skip this point and move to the next one
                    continue
                equipmenet_nbv_avg_dict[text] = x
        context['all_equipment_nvb_blbu_avg'] = equipmenet_nbv_avg_dict
        # =========== Getting the sum aqcuistion for equipments =========================
        equipmenet_acq_sum_dict = {}
        for bar in mybu:
            for baz in mybl:
                text = bar + '_' + baz
                x = db.objects.filter(BL=baz, BU=bar).aggregate(sum=Sum('acquisition_cost', output_field=IntegerField()), count=Count('acquisition_cost'))
                if x['sum'] is None:
                    continue
                equipmenet_acq_sum_dict[text] = x
        context['all_equipment_acq_blbu_sum'] = equipmenet_acq_sum_dict
        # =========== Getting the sum NBV for equipments =========================
        equipmenet_nbv_sum_dict = {}
        for bar in mybu:
            for baz in mybl:
                text = bar + '_' + baz
                x = db.objects.filter(BL=baz, BU=bar).aggregate(sum=Sum('nbv', output_field=IntegerField()), count=Count('nbv'))
                if x['sum'] is None:
                    continue
                equipmenet_nbv_sum_dict[text] = x
        print(equipmenet_nbv_sum_dict)
        context['all_equipment_nbv_blbu_sum'] = equipmenet_nbv_sum_dict

        return context

class DashboardQueryMain(ListView):
    template_name = 'dashboard/dashboard_page_query_main.html'
    context_object_name = 'dash_query_main'

    def get_queryset(self):
        return dbm.objects.all().order_by('main_date_start')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q1'] = dbm.objects.all().order_by('main_date_start')[:10]
        # ================== Count Maintenance ================
        # Get the list of clients (distinct values only)
        distinct_maintenace = dbm.objects.all().values_list('ms_type', flat=True).distinct()
        # Create dictionary to hole the key and value pairs
        main_dict = {}
        # Loop through each distinct value and assing the count of the value to it
        for bar in distinct_maintenace:
            main_dict[bar] = dbm.objects.filter(ms_type=bar).count()
        # Pass the dictionary to the context so we pass it to the html
        context['all_main_count'] = main_dict
        return context

class DashboardQueryJobs(ListView):
    template_name = 'dashboard/dashboard_page_query_job.html'
    context_object_name = 'dash_query_job_daily'
    def get_queryset(self):
        return dbj.objects.all().order_by('client')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobsQuery'] = dbj.objects.all().order_by('client')
        # ================== Count jobs per clinet ================
        # Get the list of clients (distinct values only)
        distinct_client = dbj.objects.all().values_list('client', flat=True).distinct()
        # Create dictionary to hole the key and value pairs
        clinet_dict = {}
        # Loop through each distinct value and assing the count of the value to it
        for bar in distinct_client:
            clinet_dict[bar] = dbj.objects.filter(client=bar).count()
        # Pass the dictionary to the context so we pass it to the html
        context['all_clients'] = clinet_dict
        # ================== Count jobs per BL ================
        distinct_maintenace = dbj.objects.all().values_list('BL', flat=True).distinct()
        bl_dict = {}
        for bar in distinct_maintenace:
            bl_dict[bar] = dbj.objects.filter(BL=bar).count()
        context['all_bl_count'] = bl_dict
        return context

class DashboardQueryDailyreport(ListView):
    template_name = 'dashboard/dashboard_page_query_dailyreport.html'
    context_object_name = 'dash_query_daily'

    def get_queryset(self):
        return dbd.objects.all().order_by('operationdate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dailyreport_wellname'] = dbd.objects.all().values()
        # TODO still did not find a way to filter by well
        context['report_fields'] = ['operationdate','id','whp','h2s','co2','oilrate','dp','waterrate','gasrate', 'staticp','bsw','wht','chokesize','hz','cmf','orifice']

        return context
