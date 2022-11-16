from django.urls import include,path
from django.contrib import admin

'''
app_name='TinDev'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    #path('<int:pk>/',views.PostDetailView.as_view(), name='detail'),
]
'''
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
]
