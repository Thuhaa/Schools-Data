from django.db import models

class School(models.Model):
    institute = models.CharField(max_length=200)
    building = models.CharField(max_length=200)
    floor = models.CharField(max_length=200)
    courses = models.CharField(max_length=100000)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    code = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    ownership = models.CharField(max_length=200)

    def __str__(self):
    	return self.institute
