from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
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
    path('Cand/<int:pk>/',views.CandPostDetailView.as_view(), name='CandPost'),
    #path('<int:pk>/',views.CandPostDetailView.as_view(), name='CandPost'),
    path('Rec/<int:pk>/',views.RecPostDetailView.as_view(), name='RecPost'),
    path('candidateViewPosts/', views.CandidateIndexView.as_view(), name='CandidatePosts'),
    path('delete/<int:id>/', views.delete, name='Delete'),
    path('edit/<int:id>/', views.edit, name='Edit'),
    path('post_update/', views.RecruiterIndexView.as_view(), name='Update'),
    #to like/dislike a post
    path('interested/<int:id>/', views.interest, name='interests'),
    path('not_interested/<int:id>/', views.not_interest, name='not_interests'),
    path('candidateLikedPosts/', views.candidate_likes.as_view(), name='likes'),
    path('recruiter_filter/', views.recruiter_filter, name='rec_filter'),
    path('candidate_filter/', views.candidate_filter, name='cand_filter'),
    path('offer/<int:id>/<int:pk>/', views.send_offer, name='offer'),
    path('candidateOffers/', views.CandidateOffers.as_view(), name='CandOffers'),
    path('Cand/offer/<int:pk>/', views.CandOfferDetailView.as_view(), name='CandOffer'),
    path('accept/<int:id>/', views.accept, name='Accept'),
    path('decline/<int:id>/', views.decline, name='Decline'),
]