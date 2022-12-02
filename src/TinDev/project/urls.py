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
    path('candidateDashboard/', views.candidateDashboard, name='CandidateDashboard'),
    path('recruiterDashboard/', views.recruiterDashboard, name='RecruiterDashboard'),
    path('create_post/', views.create_post, name='CreatePost'),
    path('viewAllPosts/', views.IndexView.as_view(), name='ViewAllPosts'),
    #path('<int:pk>/',views.PostDetailView.as_view(), name='Post'),
]