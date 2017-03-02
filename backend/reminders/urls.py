from django.conf.urls import url, include
from . import views

app_name = 'reminders'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^add$', views.add, name='add'),
        url(r'^(?P<reminder_slug>.*?)/$', views.detail, name='detail'),
        url(r'^(?P<reminder_slug>.*?)/delete$', views.delete, name='delete'),
]
