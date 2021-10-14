from django.urls import path
from . import views

app_name = 'fwn_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]