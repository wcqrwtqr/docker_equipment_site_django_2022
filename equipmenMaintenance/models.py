from django.db import models
from django.urls import reverse
from equipmentList.models import EQUIPMENT_DB
# Create your models here.

class MaintenanceDB(models.Model):
    main_date_start = models.DateField( null=True)
    ms_type= models.CharField(max_length=20, null=True)
    main_date_end = models.DateField(blank=True, null=True)
    main_cost = models.DecimalField(max_digits=8, null=True,decimal_places=2,blank=True)
    expiry_date = models.DateField(blank=True, null=True)
    asset = models.ForeignKey(EQUIPMENT_DB,on_delete=models.CASCADE)
    description = models.CharField(max_length=900, null=True,blank=True)
    file_link = models.URLField(max_length=200, null=True, blank=True)

    # TODO find a better way to get the total cost of the maintenacne
    @property
    def get_total_cost(self):
        temp_value = [float(cost.main_cost) for cost in self.main_cost.all()]
        return sum(temp_value)

    def get_absolute_url(self):
        """Get the url of the path

        Get the url of the path when the user click on the url

        Returns:
            url with id number
        """
        return reverse ('maintenance_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s' % (self.ms_type,self.main_date_start,self.asset)
