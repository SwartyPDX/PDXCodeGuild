from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class House(models.Model):
    house = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='house')
    member=models.ForeignKey("Member",related_name="house", on_delete=models.PROTECT)
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
    title = models.CharField('Title', max_length=40)
    desc = models.CharField('Description',blank=True, null=True, max_length=400)
    # start = models.TimeField('Start time', help_text='Start time', default='12:00')
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())
    rsvp = models.ManyToManyField('Member','event', blank=True)

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Tag(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='member')
    first=models.CharField(max_length=25)
    last = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    tag = models.ForeignKey("Tag",related_name="member", on_delete=models.PROTECT, null=True, blank=True)
    
