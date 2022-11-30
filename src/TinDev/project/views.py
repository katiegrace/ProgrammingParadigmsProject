'''


from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth import login, authenticate, logout
from project.models import UserModel
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CandidateForm, RecruiterForm, Login

# Create your views here.
# Class view for the home page


class index(View):
    def get(self, request):
        return render(request, 'project/index.html')

# Class view for creating a candidate


class create_candidate(CreateView):
    def get(self, request):
        return render(request, 'project/create_candidate.html', {'form': CandidateForm()})

    def post(self, request):
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

# Class view for creating a recruiter


class create_recruiter(CreateView):
    def get(self, request):
        return render(request, 'project/create_recruiter.html', {'form': RecruiterForm()})

    def post(self, request):
        form = RecruiterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data["password"]
            )
            user.is_recruiter = True
            form.save()
            return redirect('index')
        else:
            messages.info(request, "Count not create account.")

# Class view for a user to login


class user_login(CreateView):
    def get(self, request):
        return render(request, 'project/login.html', {'form': Login()})

    def post(self, request):
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('user_login')

# Function to logout a user and then redirect them to home page

def user_logout(request):
    logout(request)
    return redirect('index')
'''

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

def index(request):
    return render(request, 'project/index.html', {'title':'index'})
  
def login(request):
    if request.POST:
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

def candidateDashBoard(request):
    return render(request, 'project/candidateDashBoard.html', {'title':'Candidate'})

def recruiterDashBoard(request):
    return render(request, 'project/recruiterDashBoard.html', {'title':'Recruiter'})
'''
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:homepage")

'''