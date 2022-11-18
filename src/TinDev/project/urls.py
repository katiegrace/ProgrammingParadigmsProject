'''
from django.urls import path
from . import views

app_name = 'project'  # creates a namespace for this app

urlpatterns = [
     #need to create an index view for home page, before login 
     path('', views.index.as_view(), name='index'),
     path('create_candidate/', views.create_candidate.as_view(), name='create_candidate'),
     path('create_recruiter/', views.create_recruiter.as_view(),name='create_recruiter'),
     path('login/', views.user_login.as_view(), name='user_login'),
     path('logout/', views.user_logout, name='user_logout')
   #path('', views.feature1, name='index'), # the path for our index view
   #path('<int:blog_id>/', views.feature2, name='detail')
]
'''
from django.urls import path, re_path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index ),  #the path for our index view
    path('candidateProfile/', views.candidateProfile, name='CandidateProfile'),
    path('recruiterProfile/', views.recruiterProfile, name='RecruiterProfile'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    #re_path(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]