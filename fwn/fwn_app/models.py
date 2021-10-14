from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.
class Ideas(models.Model):
    title = models.CharField(max_length=40)
    tag = models.CharField(max_length=15)
    AGES = ['Baby','Toddler','Child', 'Teen', 'Adult', 'Senior']
    age = models.Choices(choices=AGES, default='Adult')
    event = models.ManyToManyField('Events','title')
    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=400)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='Attendee')
    def __str__(self):
        return self.title