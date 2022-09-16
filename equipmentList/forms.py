from .models import EQUIPMENT_DB
from django import forms

class EquipmentForm(forms.ModelForm):

    class Meta:
        bu = [('KIU', 'KIU'), ('SIU', 'SIU'), ('AGU', 'AGU'), ('NAU', 'NAU'),
              ('ADU', 'ADU')]
        bl = [('SWT', 'SWT'), ('SLS', 'SLS'), ('WHM', 'WHM'), ('DST', 'DST')]
        model = EQUIPMENT_DB
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'acquisition_date': forms.SelectDateWidget(years=[x for x in range(2009, 2025)]),
            'BU': forms.Select(choices=bu),
            'BL': forms.Select(choices=bl),
        }
