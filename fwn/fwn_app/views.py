from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from calendar import HTMLCalendar, calendar, month_name
from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from django.views import generic
import calendar
import requests
from googleapiclient import discovery
from google.oauth2.credentials import Credentials
from requests.structures import CaseInsensitiveDict
import fwn_proj.settings as settings
from oauth2client import client
import google_auth_oauthlib.flow

from .models import *
from .utils import Calendar
from .forms import *

class CalendarView(generic.ListView):
    model = Event
    template_name = 'fwn_app/cal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #call the method on the parent with super
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('fwn_app:calendar'))
    return render(request, 'fwn_app/event.html', {'form': form, 'GOOGLE_API_KEY':settings.GOOGLE_API_KEY})




def index(request):
    # return HttpResponse('ok') #test
    if request.method == 'POST':
        print(request.POST) 
        data = dict(request.POST)
        print(data)
        idea=request.POST.get('idea')
        
        return redirect('/')
    ideas = {
        'ideas':Idea.objects.all(), # get all the ideas 
    }
    print(ideas["ideas"])
    return render(request, 'fwn_app/index.html', ideas)



# def member(request):     
#     return render(request, "account/member.html",
#     {
#         'user':User.objects.all(),
        
#     })
def member(request, user_id=None):
    instance = UserProfile()
    if user_id:
        instance = get_object_or_404(UserProfile, pk=user_id)
    else:
        instance = UserProfile()

    form = UserForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('account:member'))
    return render(request, 'account/member.html', {'form': form, 'GOOGLE_API_KEY':settings.GOOGLE_API_KEY}) 


def ideaList(request):
    ideas=Idea.objects.all()
    context = {
        'ideas':ideas,
    }
    return render(request, "fwn_app/idea.html", context)
