from django.shortcuts import render, redirect
from .models import Event, Volunteer
from django.contrib.auth.decorators import login_required

@login_required
def calendar_view(request):
    if request.user.is_staff:
        events = Event.objects.all()
    else:
        events = Event.objects.filter(visibility__in=['all', request.user.groups.first().name])
    return render(request, 'calendar.html', {'events': events})
