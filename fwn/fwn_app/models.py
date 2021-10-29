from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
from django.urls import reverse
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib
# Create your models here.
#Future Household management
# class House(models.Model):
#     house = models.CharField(max_length=25)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='house')
#     member=models.ForeignKey("Member",related_name="house", on_delete=models.PROTECT)
#     def __str__(self):
#         return f'The {self.house} Family'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='profile')
    about_me = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def profile_image_url(self):
        """
        Return the URL for the user's icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        g_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='google')

        if len(g_uid):
            return "https://lh3.googleusercontent.com/a-/<g_uid>=s100"

        return "http://www.gravatar.com/avatar/{}?s=40".format(
            hashlib.md5(self.user.email).hexdigest())

    def account_verified(self):
        """
        If the user is logged in and has verified their email address, return True,
        otherwise return False
        """
        result = EmailAddress.objects.filter(email=self.user.email)
        if len(result):
            return result[0].verified
        return False


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
class Idea(models.Model):
    name = models.CharField(max_length=40)
    tag = models.ManyToManyField('Tag', 'ideas')
    desc = models.CharField(max_length=400)
    upper_age = models.IntegerField(default=110)
    lower_age = models.IntegerField(default=18)
    event = models.ManyToManyField('Event','ideas')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING , null=True, related_name='ideas')
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('Title', max_length=40)
    desc = models.CharField('Description',blank=True, null=True, max_length=400)
    # start = models.TimeField('Start time', help_text='Start time', default='12:00')
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING , null=True, related_name='event')
    def __str__(self):
        return self.title
    @property
    def get_html_url(self):
        url = reverse('fwn_app:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Tag(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

