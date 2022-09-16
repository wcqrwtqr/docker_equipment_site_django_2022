from django.db import models
from django.urls import reverse
# Create your models here.

class EQUIPMENT_DB(models.Model):
    asset_num = models.CharField(max_length=200, unique=True, blank=False)
    serial_num = models.CharField(max_length=200, unique=True, blank=True)
    description = models.CharField(max_length=800, null=True, blank=True)
    BU = models.CharField(max_length=4, null=True, blank=True)
    BL = models.CharField(max_length=4, null=True, blank=True)
    asset_life = models.IntegerField(null=True, blank=True)
    acquisition_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tot_dep_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nbv  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    acquisition_date  = models.DateField(null=True, blank=True)
    temp_location = models.CharField(max_length=200, blank=True, null=True)
    file_link = models.URLField(max_length=200, null=True, blank=True)

    # def get_absolute_url(self):
    #     return reverse('equipment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s'% (self.asset_num, self.serial_num)
    class Meta:
        ordering = ['asset_num']

