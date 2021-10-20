from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Idea, Event, House
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from calendar import HTMLCalendar, month_name
from datetime import datetime
# Create your views here.
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
        'house':House.house,
        
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
    
    return HttpResponse('ok')