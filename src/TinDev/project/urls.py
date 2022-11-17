from django.urls import path

from . import views
app_name = 'project'  # creates a namespace for this app

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('create_candidate/', views.create_candidate.as_view(),
         name='create_candidate'),
    path('create_recruiter/', views.create_recruiter.as_view(),
         name='create_recruiter'),
    path('login/', views.user_login.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout')
   #path('', views.feature1, name='index'), # the path for our index view
   #path('<int:blog_id>/', views.feature2, name='detail')
]