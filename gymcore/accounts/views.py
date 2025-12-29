import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import MemberProfile


@csrf_exempt
def signup_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    email = data.get("email")
    password1 = data.get("password1")
    password2 = data.get("password2")

    phone = data.get("phone")
    age = data.get("age")
    membership_plan = data.get("membership_plan")

    # 🔐 validations
    if not username or not password1:
        return JsonResponse({"error": "Username and password required"}, status=400)

    if password1 != password2:
        return JsonResponse({"error": "Passwords do not match"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already exists"}, status=400)

    # 1️⃣ create auth user (DB auto-handles id, date_joined, etc.)
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password1
    )

    # 2️⃣ create gym member profile
    MemberProfile.objects.create(
        user=user,
        phone=phone,
        age=age,
        membership_plan=membership_plan
    )

    return JsonResponse({
        "status": "success",
        "message": "Member registered successfully",
        "user_id": user.id
    }, status=201)


@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return JsonResponse({
            "status": "success",
            "message": "Login successful",
            "user_id": user.id
        })
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=401)


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({
        "status": "success",
        "message": "Logged out"
    })
