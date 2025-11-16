from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('submit/', views.submit_form, name='submit_form'),
    path('profile/<int:submission_id>/', views.profile_view, name='profile'),
    path('roommates/', views.roommates_list, name='roommates_list'),  

]
