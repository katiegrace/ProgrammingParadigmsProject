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
                return render(request, 'project/login.html', {"error":"Auth fail"})
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
            form.save()
        return redirect(create_post)
    return render(request, 'project/create_post.html', {'form':PostForm}) 

class IndexView(ListView):
    template_name = 'project/viewAllPosts.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        ##this is where we put the logic in for the recruiter to filter 
        return Post.objects.order_by('-expiration_date')
        #all posts- expiration date
        #active/ inactive - status
        #posts with at least 1 interested candidate - num_interested 

class PostDetailView(DetailView):
    model = Post
    template_name = 'project/post_detail.html'


'''
NEXT STEPS: update a post, delete a post
     to delete an instance from a Django data bsae Model.objects.filter(id=id).delete()
    to update an object in the Django data base Model.objects.filter(id=id).update(field=value)
'''


'''
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n form is valid")
            postition_title = CandidateProfile.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = postition_title
            new_post.save()
            return redirect('forums')
        
    context.update({
            'form': form,
            'title': 'Create New Post'
    })
    return render(request, '/create_post', context)
'''
