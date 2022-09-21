from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Avg, Max, Min, FloatField, Count, IntegerField, Sum
from equipmentList.models import EQUIPMENT_DB as db
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
        # context['q2'] = db.objects.filter(BU='SIU', BL='SLS').count
        context['q2'] = db.objects.all().values_list('BL',flat=True).distinct()
        # context['q2'] = db.objects.filter(BU='KIU').values('description').distinct()
        # context['q2'] = db.objects.all().values_list('description',flat=True).distinct()
        # context['q3'] = db.objects.filter(BU='KIU', BL='SWT').count

        context['q3'] = db.objects.filter(BL='SLS',
                                          BU='KIU').aggregate(
                                              av=Avg('acquisition_cost',
                                                     output_field=IntegerField()))

        # context['q3'] = db.objects.filter(BL='SWT',
        #                                   BU='KIU').aggregate(
        #                                       av=Avg('acquisition_cost',
        #                                              output_field=IntegerField()))

        # context['q3'] = db.objects.aggregate( Avg('acquisition_cost'))
        # context['q3'] = db.objects.aggregate( Avg('acquisition_cost'),
        #                                       Max('acquisition_cost'),
        #                                       Min('acquisition_cost'))
        # context['q4'] = db.objects.filter(BU='CEU', BL='SWT').count
        return context
