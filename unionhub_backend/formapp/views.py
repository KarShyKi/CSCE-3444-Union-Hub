from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import UserSubmission
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # allows testing from plain HTML without CSRF
def submit_form(request):
    if request.method == 'POST':
        prefix = request.POST.get('prefix', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        budget = request.POST.get('budget','')
        picture = request.FILES.get('picture', '')
        description = request.POST.get('description', '')
        submission = UserSubmission.objects.create(
            prefix=prefix,
            name=name, 
            email=email,
            phone=phone,
            budget=budget,
            picture=picture,
            description=description,

        )
        return redirect('profile', submission_id = submission.id)
    return JsonResponse({'success': False, 'error': 'POST required'})

def profile_view(request, submission_id):
    submission = get_object_or_404(UserSubmission, id = submission_id)
    return render(request, 'Roommate_profile.html', {'submission': submission})