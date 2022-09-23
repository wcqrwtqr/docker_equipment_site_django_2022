from .models import DailyreportDB
import django_filters

class DailyreportFilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = DailyreportDB
        labels= {
            'lastdayops':'Last 24hr ops',
        }
        fields = {
            'lastdayops' : ['icontains'],
        }

    def filter_by_order(self,queryset, name, value):
        expression  = 'description' if value == 'ascending' else  '-description'
        return queryset.order_by(expression)
