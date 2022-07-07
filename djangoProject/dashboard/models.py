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