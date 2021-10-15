from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Idea, Event, House
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse

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

def household(request):

    return HttpResponse('ok')

def cal(request):
    
    return HttpResponse('ok')

def idealist(request):
    
    return HttpResponse('ok')