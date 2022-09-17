import django_filters
from .models import MaintenanceDB, EQUIPMENT_DB

class Maintenancefilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = MaintenanceDB
        fields = {
            'ms_type' : ['icontains'],
            'main_cost' : ['icontains'],
            # 'asset.serial_num' : ['icontains'],
            'description' : ['icontains'],
        }
        # fields = '__all__'

    def filter_by_order(self,queryset, name, value):
        # expression  = 'description' if value == 'ascending' else  '-description'
        expression  = 'asset' if value == 'ascending' else  '-asset'
        return queryset.order_by(expression)
