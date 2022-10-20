from django.contrib.admin.options import transaction
from django.db import models
from django.urls import reverse
from equipmentList.models import EQUIPMENT_DB
import datetime
# Create your models here.

class JobsDB(models.Model):
    JOBID = models.CharField(max_length = 20 ,unique=True,blank=False)
    client = models.CharField(max_length=255,blank=False)
    field = models.CharField(max_length=255,blank=True, null=True)
    well = models.CharField(max_length=255,blank=False, null=True)
    country = models.CharField(max_length=255,blank=False,default='Iraq')
    BU = models.CharField(max_length= 3, default='KIU', null=True, blank=True)
    BL = models.CharField(max_length= 3, default='SWT', null=True, blank=True)
    description = models.CharField(max_length= 800, blank=True, null=True)
    isContract = models.BooleanField(default=True, null=True, blank=True)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(blank=True,null=True)
    h2s = models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True)
    co2 = models.DecimalField(max_digits=3,decimal_places=2,blank=True,null=True)
    oilRate = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    gasRate = models.DecimalField(max_digits=10,decimal_places=3,blank=True,null=True)

    def get_absolute_url(self):
        return reverse('jobs_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s'% (self.JOBID, self.client, self.well)

    class Meta:
        ordering = ['client']

# class JobMasterInfo(models.Model):
#     job = models.ForeignKey(JobsDB,null=True, on_delete=models.CASCADE)
#     asset = models.ManyToManyField(EQUIPMENT_DB)
#     # asset = models.ManyToManyField(EQUIPMENT_DB,null=False)

#     def get_absolute_url(self):
#         return reverse('jobs_master_info',kwargs={'pk':self.pk})

#     def __str__(self):
#         return '%s'% (self.job)

#     class Meta:
#         ordering = ['job']
