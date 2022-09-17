import django_filters
from .models import JobsDB

class Jobsfilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')
    class Meta:
        model  = JobsDB
        # fields  ="__all__"
        fields = {
            # 'JOBID' : ['icontains'], removed the unwanted fields for a smaller filter set
            'client' : ['icontains'],
            'well' : ['icontains'],
            'BU' : ['icontains'],
            'BL' : ['icontains'],
            'JOBID' : ['icontains'],
        }

    def filter_by_order(self,queryset,name, value):
        expression  = 'well' if value == 'ascending' else  '-description'
        return queryset.order_by(expression)
