#Creating calendar views using code from https://github.com/huiwenhw/django-calendar/tree/master/cal

from django.db.models.fields import CharField
from django.forms import ModelForm, DateInput, TextInput, Textarea
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'desc': Textarea(attrs={'class':"textbox"}),
      'city': TextInput(attrs={'class':"locality"}),
      'state': TextInput(attrs={'class':"administrative_area_level_1"}),
      'zipcode': TextInput(attrs={'class':"postal_code"}),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)