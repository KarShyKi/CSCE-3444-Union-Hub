from django.contrib import admin
from .models import UserSubmission

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('prefix','name', 'email', 'description', 'budget', 'picture','created_at')
    search_fields = ('name', 'email', 'phone', 'description')
    list_filter = ('budget', 'created_at')
