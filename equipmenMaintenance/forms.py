from django import forms
from .models import MaintenanceDB

from .widgets import FengyuanChenDatePickerInput
from django.forms import  DateInput

class MaintenanceForm (forms.ModelForm):
   main_date_start = forms.DateField(input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())
   main_date_end = forms.DateField(input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())
   expiry_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())

   class Meta:
      model = MaintenanceDB
      fields = '__all__'

      ms = [('MS-1','MS-1'),('MS-2','MS-2'), ('MS-3','MS-3'), ('MS-4','MS-4'),
            ('Repair','Repair'),('Down','Down'), ('Waiting on Spares','Waiting on Spares'),
            ('Junked','Junked'),
            ]

      widgets  = {
         'main_date_start' : forms.SelectDateWidget(years=[x for x in range(2018,2025)]),
         'ms_type' : forms.Select(choices=ms),
         'main_date_end' : forms.SelectDateWidget(years=[x for x in range(2018,2025)]),
         'expiry_date' : forms.SelectDateWidget(years=[x for x in range(2018,2025)]),
         'description' : forms.Textarea(attrs={'rows':3 }),

      }

# class DateForm(forms.Form):
#    main_date_start = forms.DateField(
#       input_formats=['%d-%m-%Y'],
#       widget=forms.DateInput(attrs={
#          'class': 'form-control datetimepicker-input',
#          'data-target': '#datetimepicker1'
#       })
#    )
#    main_date_end = forms.DateField(
#       input_formats=['%d-%m-%Y'],
#       widget=forms.DateInput(attrs={
#          'class': 'form-control datetimepicker-input',
#          'data-target': '#datetimepicker1'
#       })
#    )
#    expiry_date = forms.DateField(
#       input_formats=['%d-%m-%Y'],
#       widget=forms.DateInput(attrs={
#          'class': 'form-control datetimepicker-input',
#          'data-target': '#datetimepicker1'
#       })
#    )
