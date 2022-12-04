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
    path('recruiterViewAllPosts/', views.RecruiterIndexView.as_view(), name='ViewAllPosts'),
    path('<int:pk>/',views.CandPostDetailView.as_view(), name='Post'),
    path('candidateViewPosts/', views.CandidateIndexView.as_view(), name='CandidatePosts'),
    #need to change this
    path('interestedJobs/', views.CandidateIndexView.as_view(), name='Interest'),
    path('delete/<int:id>/', views.delete, name='Delete'),
    path('edit/<int:id>', views.edit, name='Edit'),
    path('post_update/', views.IndexView.as_view(), name='Update')
    
]