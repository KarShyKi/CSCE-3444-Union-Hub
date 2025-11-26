from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserSubmission


# -------------------------
# AUTHENTICATION VIEWS
# -------------------------

def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def signup_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created! Please login.")
        return redirect("login")

    return redirect("signup")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return redirect("login")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")


# -------------------------
# ROOMMATE FORM VIEWS
# -------------------------

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        prefix = request.POST.get('prefix', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        budget = request.POST.get('budget', '')
        description = request.POST.get('description', '')
        picture = request.FILES.get('picture', None)

        submission = UserSubmission.objects.create(
            prefix=prefix,
            name=name,
            email=email,
            phone=phone,
            budget=budget,
            description=description,
            picture=picture
        )
        return redirect('profile', submission_id=submission.id)

    return JsonResponse({'success': False, 'error': 'POST required'})


def profile_view(request, submission_id):
    submission = get_object_or_404(UserSubmission, id=submission_id)
    return render(request, 'Roommate_profile.html', {'submission': submission})


def home(request):
    return render(request, 'Roommate_account.html')


def roommates_list(request):
    submissions = UserSubmission.objects.all().order_by('-created_at')
    return render(request, 'Roommates.html', {'submissions': submissions})
