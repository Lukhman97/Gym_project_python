from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('main.urls')),                     # Home / Dashboard
    path('register/', include('registration.urls')),   # Registration
    # path('accounts/', include('accounts.urls')),       # Create User / Login
    path('memberships/', include('memberships.urls')), # Plans & Payments
    path('workouts/', include('workout_setup.urls')),  # Workout plans
    path('measurements/', include('measurements.urls')),# Body measurements
    path('attendance/', include('attendance.urls')),   # Attendance
]
