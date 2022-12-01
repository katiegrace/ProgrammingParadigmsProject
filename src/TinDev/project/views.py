from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from project.forms import CandidateForm
from project.models import CandidateProfile
from project.forms import RecruiterForm
from project.models import RecruiterProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
#from .models import post
#from django.views.generic import ListView

def index(request):
    return render(request, 'project/index.html', {'title':'index'})
  
def login(request):
    #This ONLY fires if someone has entered login details
    #When first opening the page, the browser will send a
    #GET request
    #This will make request.POST, which is
    #A dictionary-like object containing all given HTTP POST parameters
    #See - https://docs.djangoproject.com/en/4.1/ref/request-response/
    #Always falsey when opening the login page for the 1st time
    if request.POST:
        #This case makes sense only if these is post data
        uname = request.POST["username"]
        pwd = request.POST["password"]
        cand = CandidateProfile.objects.filter(username=uname, password=pwd)
        if cand == None:
            recruiter = RecruiterProfile.objects.filter(username=uname, password=pwd)
            if recruiter == None:
                return render(request, 'project/login.html', {"error":"Auth fail"})
            else:
                request.session["logged_user"] = uname
                return redirect("/recruiterDashboard.html")
        else:
            # the candidate authenticated
            request.session["logged_user"] = uname
            return redirect("/candidateDashboard.html")
    #The case above always return, so no need for else here
    #Also if it did not work in some edge case, the app
    #Will degrade gracefully, showing a login form instead
    #of error
    #If no post data (opening for 1st time or page reload)
    #Just render the login page
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

def candidateDashboard(request):
    return render(request, 'project/candidateDashboard.html', {'title':'Candidate'})

def recruiterDashboard(request):
    return render(request, 'project/recruiterDashboard.html', {'title':'Recruiter'})

'''
class IndexView(ListView):
    template_name = 'project/recruiterDashboard.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        ##this is where we put the logic in for the recruiter to filter 
        return Post.objects.order_by('-expiration_date')

        #all posts- expiration date
        #active/ inactive - status
        #posts with at least 1 interested candidate - num_interested 
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
    return render(request, 'forums/create_post.html', context)