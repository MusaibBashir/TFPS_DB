from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('meet', 'Meeting'),
        ('shoot', 'Shoot')
    ]
    title = models.CharField(max_length=100)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    date = models.DateField()
    visibility = models.CharField(max_length=20, default='all')
    description = models.TextField()

    def __str__(self):
        return f"{self.title} on {self.date}"

class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='volunteers')

    def __str__(self):
        return f"{self.user.username} volunteering for {self.event.title}"
