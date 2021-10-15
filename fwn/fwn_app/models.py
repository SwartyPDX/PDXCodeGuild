from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.
class House(models.Model):
    house : models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='house')

    def __str__(self):
        return f'The {self.house} Family'

class Idea(models.Model):
    name = models.CharField(max_length=40)
    tag = models.ManyToManyField('Tag', 'idea')
    desc = models.CharField(max_length=400)
    upper_age = models.IntegerField(default=110)
    lower_age = models.IntegerField(default=18)
    event = models.ManyToManyField('Event','idea')
    members = models.ManyToManyField('House','idea')
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=400)
    date = models.DateField()
    rsvp = models.ManyToManyField('House','event')
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name