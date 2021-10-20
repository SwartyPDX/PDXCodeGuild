from django.urls import path
from . import views

# Need calendar path with date and UUID
app_name = 'fwn_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<str:month>',views.calendar, name='calendar'),
    path('<house>',views.calendar, name='calendar'),

]