from django.contrib import admin
from django.contrib import admin
from .models import Idea, Event, House,Tag
admin.site.register(Idea)
admin.site.register(Event)
admin.site.register(House)
admin.site.register(Tag)