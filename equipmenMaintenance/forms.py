from django import forms
from .models import MaintenanceDB


class MaintenanceForm (forms.ModelForm):
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
