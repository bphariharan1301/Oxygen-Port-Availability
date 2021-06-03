from django.db import models

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=100, blank=False)
    address = models.TextField()
    state = models.CharField(max_length=100, blank=True, default="State")
    district = models.CharField(max_length=100, blank=True, default="District")
    total_oxygen_bed = models.IntegerField(default=0)
    occupied_oxygen_bed = models.IntegerField(default=0)
    vaccant_oxygen_bed = models.IntegerField(default=0)
    total_ICU_bed = models.IntegerField(default=0)
    occupied_ICU_bed = models.IntegerField(default=0)
    vaccant_ICU_bed = models.IntegerField(default=0)
    total_normal_bed = models.IntegerField(default=0)
    occupied_normal_bed = models.IntegerField(default=0)
    vaccant_normal_bed = models.IntegerField(default=0)
    total_ventilator_bed = models.IntegerField(default=0)
    occupied_ventilator_bed = models.IntegerField(default=0)
    vaccant_ventilator_bed = models.IntegerField(default=0)
    total_bed = models.IntegerField(default=0)
    total_occupied_bed = models.IntegerField(default=0)
    total_vaccant_bed = models.IntegerField(default=0)

    def __str__(self):
        return self.name

