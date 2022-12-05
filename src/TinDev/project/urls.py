from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
#app_name='project'
urlpatterns = [
    path('', views.index ),  #the path for our index view
    path('candidateProfile/', views.candidateProfile, name='CandidateProfile'),
    path('recruiterProfile/', views.recruiterProfile, name='RecruiterProfile'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('candidateDashboard/', views.candidateDashboard, name='CandidateDashboard'),
    path('recruiterDashboard/', views.recruiterDashboard, name='RecruiterDashboard'),
    path('create_post/', views.create_post, name='CreatePost'),
    path('recruiterViewAllPosts/', views.RecruiterIndexView.as_view(), name='Vie    wAllPosts'),
    path('Cand/<int:pk>/',views.CandPostDetailView.as_view(), name='CandPost'),
    #path('<int:pk>/',views.CandPostDetailView.as_view(), name='CandPost'),
    path('Rec/<int:pk>/',views.RecPostDetailView.as_view(), name='RecPost'),
    path('candidateViewPosts/', views.CandidateIndexView.as_view(), name='CandidatePosts'),
    #need to change this
    path('delete/<int:id>/', views.delete, name='Delete'),
    path('edit/<int:id>/', views.edit, name='Edit'),
    path('post_update/', views.RecruiterIndexView.as_view(), name='Update'),
    #to like/dislike a post
    path('interested/<int:id>/', views.interest, name='interests'),
    path('not_interested/<int:id>/', views.not_interest, name='not_interests'),
    path('candidateLikedPosts/', views.candidate_likes.as_view(), name='likes'),
    
]