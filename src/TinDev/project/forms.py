from django.forms import ModelForm
from django import forms
from .models import CandidateProfile
from .models import RecruiterProfile
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Offer

class CandidateForm(ModelForm):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    bio = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder': 'Bio', 'style': 'width: 300px;', 'class': 'form-control'}))
    zipcode = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Zipcode', 'style': 'width: 300px;', 'class': 'form-control'}))
    skills = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder': 'Skills', 'style': 'width: 300px;', 'class': 'form-control'}))
    git_username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Github', 'style': 'width: 300px;', 'class': 'form-control'}))
    years_exp = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'placeholder': 'Experience', 'style': 'width: 300px;', 'class': 'form-control'}))
    username =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = CandidateProfile
        fields = ['name', 'bio', 'zipcode', 'skills', 'git_username', 'years_exp', 'username', 'password']

class RecruiterForm(ModelForm):

    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    company = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'placeholder': 'Company', 'style': 'width: 300px;', 'class': 'form-control'}))
    zipcode = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Zipcode', 'style': 'width: 300px;', 'class': 'form-control'}))
    username =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}))
    
    class Meta:
        model = RecruiterProfile
        fields = ['name', 'company', 'zipcode','username','password']


class PostForm(ModelForm):
    position_title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    position_type = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Type (Full/Part)', 'style': 'width: 300px;', 'class': 'form-control'}))
    location = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Location (City, State)', 'style': 'width: 300px;', 'class': 'form-control'}))
    preferred_skills = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Skills', 'style': 'width: 300px;', 'class': 'form-control'}))
    description = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Description', 'style': 'width: 300px;', 'class': 'form-control'}))
    company = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Company', 'style': 'width: 300px;', 'class': 'form-control'}))
    expiration_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'Date (mm/dd/yyyy)', 'style': 'width: 300px;', 'class': 'form-control'}))
    status = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Status (Active/Inactive)', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['position_title', 'position_type', 'location', 'preferred_skills', 'description', 'company', 'expiration_date', 'status']

class OfferForm(ModelForm):
    salary_info = forms.CharField(max_length=200, widget = forms.TextInput(attrs={'placeholder': 'Salary', 'style': 'width: 300px;', 'class': 'form-control'}))
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'Due Date (mm/dd/yyyy)', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = Offer
        fields = ['salary_info', 'due_date']