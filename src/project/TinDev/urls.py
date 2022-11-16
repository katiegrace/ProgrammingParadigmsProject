from django.urls import path
from . import views

'''
app_name='TinDev'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    #path('<int:pk>/',views.PostDetailView.as_view(), name='detail'),
]
'''

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
 
urlpatterns = [
         path('', views.index, name='index'),
]
