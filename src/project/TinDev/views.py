from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template
from .forms import CandidateForm, RecruiterForm, Login
from project.models import UserModel


#################### index#######################################
class index(View):
    def get(self, request):
        return render(request, 'project/index.html', {'title':'index'})
  
########### register here #####################################
'''def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            d = { 'username': username }
            html_content = htmly.render(d)
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'register here'}) '''
################ candidate/recruiter forms###################################################
class create_candidate(CreateView):
    def get(self, request):
        return render(request, 'project/create_candidate.html', {'form': CandidateForm()})

    def post(self, request):
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

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

################ login/out forms###################################################
class user_login(request):
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

def user_logout(request):
    logout(request)
    return redirect('index')