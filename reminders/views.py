from datetime import datetime, timedelta
from django.http import HttpResponseRedirect as redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Reminder
from .serializers import ReminderSerializer

def index(request):
    reminders = Reminder.objects.all()[3:]
    upcoming = Reminder.objects.all()[0:3]
    return render(request, 'reminders/index.html', {'upcoming': upcoming, 'reminders': reminders})

def detail(request, reminder_slug):
    reminder = get_object_or_404(Reminder, slug=reminder_slug)
    return render(request, 'reminders/detail.html', {'reminder': reminder})

def add(request):
    r = Reminder()
    r.publish_date = datetime.utcnow()
    r.run_date = datetime.utcnow() + timedelta(hours=1)
    r.text = request.POST.get('reminder_text', 'Nothing got sent yo!')
    r.save()
    return redirect('/reminders/')

def delete(request, reminder_slug):
    reminder = get_object_or_404(Reminder, slug=reminder_slug)
    reminder.delete()
    return redirect('/reminders/')

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def json_detail(request, reminder_slug):
    try:
        reminder = Reminder.objects.get(slug=reminder_slug)
    except Reminder.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReminderSerializer(reminder)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReminderSerializer(reminder, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        reminder.delete()
        return HttpResponse(status=204)

@csrf_exempt
def json_index(request):
    if request.method == 'GET':
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
