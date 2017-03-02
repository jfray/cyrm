from django.conf.urls import include, url
from . import views

app_name = 'reminders'

urlpatterns = [
        url(r'^$', views.json_index, name='json_index'),
        url(r'^(?P<reminder_slug>.*?)/$', views.json_detail, name='json_detail'),
]
