from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import  redirect, render
from django.http import HttpResponse

@login_required
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home') 
            else:
                return HttpResponse("<script>alert('Your account is inactive.');window.location.href='/';</script>")
        else:
             return HttpResponse("<script>alert('Invalid login details.');window.location.href='/';</script>")
    return render(request, 'login.html')
