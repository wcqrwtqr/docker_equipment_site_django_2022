from django.contrib.admin.options import transaction
from django.db import models
from django.urls import reverse
from equipmentList.models import EQUIPMENT_DB
import datetime
# Create your models here.

class JobsDB(models.Model):
    JOBID = models.CharField(max_length = 20 ,unique=True,blank=False)
    gen_JOBID = models.CharField(max_length = 20 ,unique=False,blank=True)
    get_id = models.CharField(max_length=10,default="", blank=True)
    client = models.CharField(max_length=255,blank=False)
    tag_client = models.CharField(max_length=5,blank=True, null=True)
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
    updated = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    file_link = models.URLField(max_length=200, null=True, blank=True)

    @property
    def id_getting(self):
        return str(self.id)

    @property
    def get_gen_JOBID(self):
        a = self.BU
        b = self.BL
        c = self.tag_client
        d = self.id_getting
        return '%s-%s-%s-%s'% (a , b, c, d )

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            self.get_id = self.id_getting
            self.gen_JOBID = self.get_gen_JOBID
            super().save(*args, **kwargs)

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
