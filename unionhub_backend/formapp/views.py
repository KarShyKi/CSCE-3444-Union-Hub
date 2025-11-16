from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserSubmission

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