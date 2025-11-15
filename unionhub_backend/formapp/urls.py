from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_form, name='submit_form'),
    path('profile/<int:submission_id>/', views.profile_view, name ='profile'),
]
