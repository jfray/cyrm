from django.conf.urls import include, url
from django.contrib import admin
from reminders import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/$', views.json_index, name='json_index'),
    url(r'api/(?P<reminder_slug>.*?)/$', views.json_detail, name='json_detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^reminders/', include('reminders.urls')),
]
