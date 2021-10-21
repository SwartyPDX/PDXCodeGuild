from django.urls import path
from django.conf.urls import url
from . import views

# Need calendar path with date and UUID
app_name = 'fwn_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/$', views.CalendarView.as_view(), name='calendar'),
    path('<int:year>/<str:month>',views.calendar, name='calendar'),
    path('<house>',views.household, name='house'),

]