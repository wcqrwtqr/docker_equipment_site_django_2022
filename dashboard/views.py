from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Avg, Max, Min, FloatField, Count, IntegerField, Sum
from equipmentList.models import EQUIPMENT_DB as db
# import pandas as pd
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
        mybu = ['KIU', 'SIU' ]
        mybl = ['SWT', 'SLS'  ]
        mylabel=[]
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
