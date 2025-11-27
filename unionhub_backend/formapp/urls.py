from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('signup_user/', views.signup_user, name='signup_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # ROOMMATE
    path('roommate_account/', views.home, name='roommate_account'),
    path('submit/', views.submit_form, name='submit_form'),
    path('profile/<int:submission_id>/', views.profile_view, name='profile'),
    path('roommates/', views.roommates_list, name='roommates'),

    # LOST & FOUND (ORDER MATTERS)
    path("lost-found/", views.lost_found_list, name="lost_found_list"),  
    path("lost-found/submit/", views.lost_found_submit, name="lost_found_form"),
    path("lost-found/item/<int:id>/", views.lost_found_item, name="lost_found_item"),
    path("lost-found/edit/<int:id>/", views.edit_lost_found_item, name="lost_found_edit"),
]
