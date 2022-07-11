from time import time
from django.db import models
from django.utils import timezone

# Create your models here.
class Schedule(models.Model):
    date = models.DateTimeField(default=timezone.now)
    activity = models.TextField()
    person = models.CharField(max_length=50)
    STATUS = (
        ('Preparation','Preparation'),
        ('Done','Done'),
        ('Rescheduled','Rescheduled'),
        ('Cancelled','Cancelled'),
    )
    schedule_status = models.CharField(max_length=50,choices=STATUS)

class ConsultantStatus(models.Model):
    name_of_professional = models.CharField(max_length=50)
    CONSULTANT_STATUS = (
        ('Yes','Yes'),
        ('No','No'),
    )
    consultant_status = models.CharField(max_length=50,choices=CONSULTANT_STATUS)
    TYPE_OF_LICENSE = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('No License','No License'),
    )
    type_of_license = models.CharField(max_length=50,choices=TYPE_OF_LICENSE)
    expired_date = models.DateTimeField()

class LawyerStatus(models.Model):
    name_of_professional = models.CharField(max_length=50)
    LAWYER_STATUS = (
        ('Yes','Yes'),
        ('No','No'),
    )
    lawyer_status = models.CharField(max_length=50,choices=LAWYER_STATUS)
    license_number = models.CharField(max_length=50)
    expired_date = models.DateTimeField()