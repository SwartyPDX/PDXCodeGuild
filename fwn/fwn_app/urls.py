from django.urls import path
from . import views
from datetime import datetime

now=datetime.now

app_name = 'fwn_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('member/', views.member, name='member'),

    # path('<int:year>/<str:month>',views.calendar, name='calendar'),
    # path('<house>',views.household, name='house'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<event_id>/', views.event, name='event_edit'),
    path('accounts/profile/',views.index, name='accounts')
]