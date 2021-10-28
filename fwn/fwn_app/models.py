from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#Future Household management
# class House(models.Model):
#     house = models.CharField(max_length=25)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='house')
#     member=models.ForeignKey("Member",related_name="house", on_delete=models.PROTECT)
#     def __str__(self):
#         return f'The {self.house} Family'

class Idea(models.Model):
    name = models.CharField(max_length=40)
    tag = models.ManyToManyField('Tag', 'idea')
    desc = models.CharField(max_length=400)
    upper_age = models.IntegerField(default=110)
    lower_age = models.IntegerField(default=18)
    event = models.ManyToManyField('Event','idea')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING , null=True, related_name='idea')
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('Title', max_length=40)
    desc = models.CharField('Description',blank=True, null=True, max_length=400)
    # start = models.TimeField('Start time', help_text='Start time', default='12:00')
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING , null=True, related_name='event')

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Tag(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

