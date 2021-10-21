from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from calendar import HTMLCalendar, month_name
from datetime import datetime , timedelta, date
from django.utils.safestring import mark_safe
from django.views import generic

from .models import *
from .utils import Calendar
from .forms import EventForm


#Creating calendar views using code from https://github.com/huiwenhw/django-calendar/tree/master/cal
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
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})




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

def household(request, profile):
    return render(request, "fwn_app/house.html",
    {
        'house':House,
        
    })
   

def calendar(request, year, month):
    uuid= User
    month = month.capitalize()
    month_num = list(month_name).index(month)
    month_num=int(month_num)
    now= datetime.now()
    current_year=now.year
    cal= HTMLCalendar().formatmonth(year, month_num)
    return render(request, "fwn_app/cal.html",
    {
        "year" : year,
        "month" : month,
        "uuid" : uuid,
        "cal":cal,
        "current_year":current_year
    })

def idealist(request):
    return render(request, "fwn_app/idea.html",
    {
        'idea':Idea,
        
    })
