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
        UserSubmission.objects.create(
            prefix=prefix,
            name=name, 
            email=email,
            phone=phone,
            budget=budget,
            picture=picture,
            description=description,

        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'POST required'})
