from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Load_and_found_submission
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



# -------------------------
# LOST AND FOUND VIEWS
# -------------------------

def lost_found_list(request):
    items = Load_and_found_submission.objects.all().order_by('-id')
    return render(request, "Lost_and_found_items.html", {"items": items})


def lost_found_item(request, id):
    item = get_object_or_404(Load_and_found_submission, id=id)
    return render(request, "Lost_and_found_item.html", {"item": item})


def lost_found_submit(request):
    if request.method == "POST":
        item_picture = request.FILES.get('item_picture')
        item_desc = request.POST.get('item_desc')
        item_name = request.POST.get('item_name')
        item_found = request.POST.get('item_found')
        item_submitted = request.POST.get('item_submitted')
        item_contact = request.POST.get('item_contact')

        item = Load_and_found_submission.objects.create(
            item_picture=item_picture,
            item_desc=item_desc,
            item_name=item_name,
            item_found=item_found,
            item_submitted=item_submitted,
            item_contact=item_contact
        )

        return redirect("lost_found_item", id=item.id)

    return render(request, "Lost_and_found_account.html")


def edit_lost_found_item(request, id):
    item = get_object_or_404(Load_and_found_submission, id=id)

    if request.method == "POST":
        item.item_name = request.POST.get("item_name")
        item.item_desc = request.POST.get("item_desc")
        item.item_found = request.POST.get("item_found")
        item.item_submitted = request.POST.get("item_submitted")
        item.item_contact = request.POST.get("item_contact")

        if request.FILES.get("item_picture"):
            item.item_picture = request.FILES["item_picture"]

        item.save()
        return redirect("lost_found_item", id=item.id)

    return render(request, "Lost_and_found_account.html", {
        "item": item,
        "edit": True
    })
