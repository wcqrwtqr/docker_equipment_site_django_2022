from django.contrib.admin.options import widgets
from django.contrib.admin.utils import label_for_field
from django.utils.autoreload import start_django
from .models import DailyreportDB
from django import forms
from .widgets import FengyuanChenDatePickerInput
from django.forms import  DateInput

class DailyForm(forms.ModelForm):
    operationdate = forms.DateField(label="Date",input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput()) # h2s = forms.DecimalField(label="H2S")

    class Meta:
        model = DailyreportDB
        fields = '__all__'
        labels = {
            'lastdayops' : "Last Day Operation",
            'nextdayops' : "Next Day Operation",
            'jobid' : "Job ID",
            'h2s' :"H2S",
            'co2' : "CO2",
            'oilrate' :"Oil Rate",
            'waterrate' :"Water rate",
            'dp' :"Diff Pressure",
            'staticp' :"Static pressure",
            'gasrate' :"Gas Rate",
            'orifice' :"Orifice Size",
            'cmf' :"CMF",
            'whp' :"WHP",
            'todayproduced' :"Daily Production",
            'totalproduction' :"Total Production",
            'wht' :"WHT",
            'bsw' :"BSW",
            'flowduration' :"Flow Durtion",
            'chokesize' :'Choke Size 1/64"',
            'supervisorname' :"Superviosr Name",
            'isESP' :"ESP",
            'isDST' :"DST",
            'isSLS' :"SLS",
            'isSWT' :"SWT",
            'isCleanup' :"Clean up",
            'isProduction' :"Production",
        }
        widgets = {
            'lastdayops': forms.Textarea(attrs={'rows': 3}),
            'nextdayops': forms.Textarea(attrs={'rows': 3}),
            "isSLS" : forms.CheckboxInput(),
            "isSWT" : forms.CheckboxInput(),
            "isDST" : forms.CheckboxInput(),
            "isESP" : forms.CheckboxInput(),
            "isCleanup" : forms.CheckboxInput(),
            "isProduction" : forms.CheckboxInput(),
        }


# class DateForm(forms.Form):
#    acquisition_date = forms.DateField(
#       input_formats=['%d-%m-%Y'],
#       widget=forms.DateInput(attrs={
#          'class': 'form-control datetimepicker-input',
#          'data-target': '#datetimepicker1'
#       })
#    )
