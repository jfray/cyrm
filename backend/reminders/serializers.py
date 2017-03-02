from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('slug', 'text', 'publish_date', 'run_date')
        model = Reminder
