from django.contrib import admin
from django.urls import path
from events.views import calendar_view, volunteer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar/', calendar_view, name='calendar'),
    path('volunteer/<int:event_id>/', volunteer, name='volunteer'),
]
