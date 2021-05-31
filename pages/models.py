from django.db import models

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.TextField()
    total_oxygen_bed = models.IntegerField(default=0)
    vaccant_oxygen_bed = models.IntegerField(default=0)
    total_ICU_bed = models.IntegerField(default=0)
    vaccant_ICU_bed = models.IntegerField(default=0)
    total_covid_bed = models.IntegerField(default=0)
    vaccant_covid_bed = models.IntegerField(default=0)
    total_ventilator_bed = models.IntegerField(default=0)
    vaccant_ventilator_bed = models.IntegerField(default=0)

