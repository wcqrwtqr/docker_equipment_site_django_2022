import django_filters
# from equipmentMaintenance.models import MaintenanceDB
from .models import EQUIPMENT_DB

class EquipmentFilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = EQUIPMENT_DB
        fields = {
            'serial_num' : ['icontains'],
            'description' : ['icontains'],
            'BU' : ['icontains'],
            'BL' : ['icontains'],
        }

    def filter_by_order(self,queryset, name, value):
        expression  = 'description' if value == 'ascending' else  '-description'
        return queryset.order_by(expression)

# class EquipmentMaintenanceFilter(django_filters.FilterSet):
#     CHOICES = [
#         ('ascending','Ascending'),
#         ('descending','Descending'),
#     ]
#     ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

#     class Meta:
#         model  = MaintenanceDB
#         fields = '__all__'

#     def filter_by_order(self,queryset, name, value):
#         expression  = 'description' if value == 'ascending' else  '-description'
#         return queryset.order_by(expression)
