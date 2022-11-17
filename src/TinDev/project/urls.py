from django.urls import path
from . import views

app_name = 'project'  # creates a namespace for this app

urlpatterns = [
     #need to create an index view for home page, before login 
     path('', views.index.as_view(), name='index'),
     path('accounts/', include('django.contrib.auth.urls')),
     #takes you to an an account home page which allows you to choose what type you are signing up for
     path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
     #student candidate up screen
     path('accounts/signup/candidate/', views.CandidateSignUpView.as_view(), name='candidate_signup'),
     #recruiter sign up page
     path('accounts/signup/recruiter/', views.RecruiterSignUpView.as_view(), name='recruiter_signup'),
     #log in page
     path('accounts/login/', views.LogIn.as_view(), name='login'),
     #log out page
     path('accounts/logout/', views.logout.as_view(), name='logout'),
   #path('', views.feature1, name='index'), # the path for our index view
   #path('<int:blog_id>/', views.feature2, name='detail')
]
