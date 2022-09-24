from .models import EQUIPMENT_DB
from django import forms
from .widgets import FengyuanChenDatePickerInput
from django.forms import  DateInput

class EquipmentForm(forms.ModelForm):
    acquisition_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())
    class Meta:
        bu = [('KIU', 'KIU'), ('SIU', 'SIU'), ('AGU', 'AGU'), ('NAU', 'NAU'),
              ('ADU', 'ADU')]
        bl = [('SWT', 'SWT'), ('SLS', 'SLS'), ('WHM', 'WHM'), ('DST', 'DST')]
        model = EQUIPMENT_DB
        fields = '__all__'
        labels = {
            'asset_num': 'Asset No',
            'serial_num': 'Serial No',
            'description': 'Description',
            'asset_life': 'Asset Life',
            'acquisition_cost': 'Purchase Cost',
            'tot_dep_value': 'Depreciation',
            'nbv ': 'NBV',
            'acquisition_date ': 'Purchase Date',
            'temp_location': 'Location',
            'file_link': 'Link',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'BU': forms.Select(choices=bu),
            'BL': forms.Select(choices=bl),
        }



# class DateForm(forms.Form):
#    acquisition_date = forms.DateField(
#       input_formats=['%d-%m-%Y'],
#       widget=forms.DateInput(attrs={
#          'class': 'form-control datetimepicker-input',
#          'data-target': '#datetimepicker1'
#       })
#    )
