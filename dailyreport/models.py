from jobs.models import JobsDB
# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

class DailyreportDB(models.Model):

    jobid = models.ForeignKey(JobsDB,on_delete=models.CASCADE)
    operationdate  = models.DateField(null=False, blank=True)
    lastdayops = models.CharField(max_length=2500, null=True, blank=True)
    nextdayops = models.CharField(max_length=2500, null=True, blank=True)
    h2s = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    co2 = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    oilrate = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    waterrate = models.IntegerField(blank=True,null=True)
    dp = models.IntegerField(blank=True,null=True)
    staticp = models.IntegerField(blank=True,null=True)
    gasrate = models.DecimalField(max_digits=10,decimal_places=4,blank=True,null=True)
    orifice = models.DecimalField(max_digits=5,decimal_places=3,blank=True,null=True)
    cmf = models.DecimalField(max_digits=5,decimal_places=3,blank=True,null=True)
    whp = models.IntegerField(blank=True,null=True)
    todayproduced = models.IntegerField(blank=True,null=True)
    totalproduction = models.IntegerField(blank=True,null=True)
    wht = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    bsw = models.DecimalField(max_digits=5,decimal_places=2,blank=True,null=True)
    hz = models.IntegerField(blank=True,null=True)
    flowduration = models.IntegerField(blank=True,null=True)
    chokesize = models.IntegerField(blank=True,null=True)
    supervisorname = models.CharField(max_length=200,  blank=False)
    isESP = models.BooleanField(default=False, null=True, blank=True)
    isDST = models.BooleanField(default=False, null=True, blank=True)
    isSLS = models.BooleanField(default=False, null=True, blank=True)
    isSWT = models.BooleanField(default=True, null=True, blank=True)
    isCleanup = models.BooleanField(default=True, null=True, blank=True)
    isProduction = models.BooleanField(default=True, null=True, blank=True)

    # def get_absolute_url(self):
    #     return reverse('equipment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s %s'% (self.jobid, self.operationdate, self.supervisorname)
    class Meta:
        ordering = ['operationdate']
