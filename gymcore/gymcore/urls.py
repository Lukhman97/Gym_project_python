from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('',include('registration.urls')),
    path('',include('measurements.urls')),
    path('',include('workout_setup.urls')),
    path('',include('attendance.urls')),
    path('',include('memberships.urls')),
]

