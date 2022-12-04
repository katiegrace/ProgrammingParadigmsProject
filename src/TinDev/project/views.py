from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from project.forms import CandidateForm
from project.models import CandidateProfile
from project.forms import RecruiterForm
from django.views.generic import ListView, DetailView
from project.models import RecruiterProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from project.forms import Post
from .forms import Post
from .forms import PostForm
#from .models import post
#from django.views.generic import ListView

def index(request):
    return render(request, 'project/index.html', {'title':'index'})
  
def login(request):
    #This ONLY works if someone has entered login details
    #When first opening the page, the browser will send a GET request
    #This will make request.POST, which is similar to a dict
    if request.POST:
        #This case makes sense only if these is post data
        uname = request.POST["username"]
        pwd = request.POST["password"]
        cand = CandidateProfile.objects.filter(username=uname, password=pwd)
        #len(cand) will be 0 if no candidates found and we need to check recruiters
        if len(cand) == 0:
            recruiter = RecruiterProfile.objects.filter(username=uname, password=pwd)
            #len(recruiter) will be 0 if no recruiters found
            if len(recruiter) == 0:
                return render(request, 'project/login.html', {"error":"Incorrect username or password"})
            else:
                #We should have 0 or 1, never more
                assert len(recruiter) > 0
                request.session["logged_user"] = uname
                return redirect("/recruiterDashboard")
        else:
                #We should have 0 or 1 candidates, never more
            assert len(cand) > 0
                # the candidate authenticated
            request.session["logged_user"] = uname
                #redirect to candidate dashboard
            return redirect("/candidateDashboard")
    # shows a login form instead of error
    return render(request, 'project/login.html')
    

def logout(request):
    del request.session["logged_user"]
    return redirect("/login")

def candidateProfile(request):
    if request.POST:
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(login)
    return render(request, 'project/candidateProfile.html', {'form':CandidateForm}) 

def recruiterProfile(request):
    if request.POST:
        form = RecruiterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(login)
    return render(request, 'project/recruiterProfile.html', {'form':RecruiterForm}) 

# added context for scaalbility, before it said {'title':'Candidate'} but added context dictionary
def candidateDashboard(request):
    context={
        'home_page': "active",
    }
    return render(request, 'project/candidateDashboard.html', {'title':'Candidate'} )

def recruiterDashboard(request):
    context={
        'home_page': "active",
    }
    return render(request, 'project/recruiterDashboard.html',{'title':'Recruiter'} )

'''
dont know if u need this 
    # redirct to view all posts
        return redirect("/viewAllPosts")
        #return redirect(create_post)
        by line 100
'''

def create_post(request):
    
    if request.POST:
        form = PostForm(request.POST)
        
        if form.is_valid():
            recruiter = RecruiterProfile.objects.filter(username=request.session['logged_user'])[0]
            form.instance.recruiter = recruiter
            form.save()
            
            print(form.instance)
            # filter returns an array either 
            return redirect("/recruiterViewAllPosts")
        else:
            #Add proper error reporting to the user
            #raise ValueError(f"Form is not valid, errors {form.errors}")
            return render(request, 'project/create_post.html', {'form':form,"error":"Form is invalid"})
        #if they create a post we want it to take them to view all posts 
    return render(request, 'project/create_post.html', {'form':PostForm}) 



class CandidateIndexView(ListView):
    template_name = 'project/candidateViewPosts.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        print(Post.objects.all().order_by('-expiration_date'))
        return (Post.objects.all().order_by('-expiration_date'))
    
class RecruiterIndexView(ListView):
    template_name = 'project/recruiterViewAllPosts.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        #filter all the post objects to only include those in which in recruiter's username matched the one logged in
        uname_id = RecruiterProfile.objects.filter(username=self.request.session['logged_user'])[0]
        #need to do return (Post.objects.filter(recruiter.username = uname).order_by('-expiration_date'))
        return (Post.objects.filter(recruiter= uname_id).order_by('-expiration_date'))

class CandPostDetailView(DetailView):
    model = Post
    template_name = 'project/base_post_detail.html'

def RecPostDetailView(DetailView):
    model = Post
    template_name = 'project/rec_post_detail.html'

def delete(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return redirect('/recruiterViewAllPosts')

def edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)

        if form.is_valid():
            form.save()
            return redirect("/recruiterViewAllPosts")
    else:
        form = PostForm(instance=post)
    #if they create a post we want it to take them to view all posts 
    return render(request, 'project/post_update.html', {'form':form})
    return redirect('')