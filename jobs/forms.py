from django.contrib.admin.options import widgets
from django.utils.autoreload import start_django
from .models import JobsDB
from django import forms

from .widgets import FengyuanChenDatePickerInput
from django.forms import DateTimeInput, DateInput

class JobsForm(forms.ModelForm):
    startDate = forms.DateField(label="Start Date", input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())
    endDate = forms.DateField(label="End Date",input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())
    class Meta:
        model = JobsDB
        fields = '__all__'
        exclude = ['get_id','gen_JOBID']

        bu = [('KIU','KIU'),('SIU','SIU'), ('AGU','AGU'), ('NAU','NAU'), ('ADU','ADU'),]
        bl = [('SWT','SWT'),('SLS','SLS'), ('WHM','WHM'), ('DST','DST'),]

        labels = {

            'JOBID' :'Job ID',
            'client' :'Client',
            'tag_client' :'Taq of Client',
            'field' :'Field',
            'well' :'Well',
            'country' :'Country',
            'description' :'Description',
            'h2s' :'H2S',
            'co2' :'CO2',
            'oilRate' :'Oil Rate',
            'gasRate' :'Gas Rate',
            'file_link' :'Link',

        }
        widgets  = {
            'description' : forms.Textarea(attrs={'rows':3 }),
            # 'startDate' : forms.SelectDateWidget(years=[x for x in range(2013,2025)]),
            # 'endDate' : forms.SelectDateWidget(years=[x for x in range(2013,2025)]),
            'BU' : forms.Select(choices=bu),
            'BL' : forms.Select(choices=bl),
        }


# class DateForm(forms.Form):
#     startDate = forms.DateField(
#         # input_formats=['%Y-%M-%d'],
#         input_formats=['%d-%m-%Y'],
#         widget=forms.DateInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
#     endDate = forms.DateField(
#         input_formats=['%d-%m-%Y'],
#         widget=forms.DateInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
#
# class JobsEquipmentForm(forms.ModelForm):
#     class Meta:
#         model = JobMasterInfo
#         fields = '__all__'
# fields = ['job', 'asset']

        # # job = forms.CharField()
        # asset = forms.ModelMultipleChoiceField(
        #     queryset=JobMasterInfo.objects.all(),
        #     widget=forms.CheckboxSelectMultiple
        # )
