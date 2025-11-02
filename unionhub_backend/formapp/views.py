from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import UserSubmission
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # allows testing from plain HTML without CSRF
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        UserSubmission.objects.create(name=name, email=email)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'POST required'})
