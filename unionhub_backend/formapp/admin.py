from django.contrib import admin
from .models import UserSubmission, Load_and_found_submission

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('prefix','name', 'email', 'description', 'budget', 'picture','created_at')
    search_fields = ('name', 'email', 'phone', 'description')
    list_filter = ('budget', 'created_at')

@admin.register(Load_and_found_submission)
class LostAndFoundAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_found', 'item_submitted', 'item_contact')
    search_fields = ('item_name', 'item_found', 'item_submitted', 'item_contact')
    list_filter = ('item_found', 'item_submitted')