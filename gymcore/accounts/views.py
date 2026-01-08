from datetime import datetime, date
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AttendanceRecord
from .forms import AttendanceForm
from django.utils import timezone

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('attendance_stats')
    else:
        form = AttendanceForm(user=request.user)
    return render(request, 'attendance/mark_attendance.html', {'form': form})

@login_required
def attendance_stats(request):
    user = request.user
    records = AttendanceRecord.objects.filter(user=user)
    return render(request, 'attendance/attendance_stats.html', {'records': records})

@login_required
def attendance_totalstats_today(request):
    today = date.today()
    records = AttendanceRecord.objects.filter(date=today)
    count = records.count() 
    return HttpResponse(f"<script>alert('{count}');window.location.replace('/home');</script>")


def attendance_totalstats(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    records = AttendanceRecord.objects.filter(date__month=current_month, date__year=current_year)
    count = records.count() 
    return HttpResponse(f"<script>alert('{count}');window.location.replace('/home');</script>")
