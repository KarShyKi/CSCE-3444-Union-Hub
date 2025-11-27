from django.db import models

BUDGET_CHOICES = [
    ('<500', 'Under $500'),
    ('500-1000', '$500 - $1,000'),
    ('1000-1500', '$1,000 - $1,500'),
    ('1500-2000', '$1,500 - $2,000'),
    ('2000-2500', '$2,000 - $2,500'),
    ('>2500', 'Above $2,500'),
]
# Create your models here.
class UserSubmission(models.Model):
    prefix = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES)
    description = models.TextField()
    picture = models.ImageField(upload_to ='submission/', blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
#for lost and found item
class Load_and_found_submission(models.Model):
    item_picture = models.ImageField(upload_to ='submission/', blank=True, null = True)
    item_desc = models.TextField()
    item_name = models.CharField(max_length=100)
    item_found = models.CharField(max_length=100)
    item_submitted = models.CharField(max_length=100)
    item_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.item_name
