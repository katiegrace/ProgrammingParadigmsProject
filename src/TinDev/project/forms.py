from django.forms import ModelForm
from django import forms
from .models import CandidateProfile
from .models import RecruiterProfile
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class CandidateForm(ModelForm):
    name = forms.CharField(max_length=200)
    bio = forms.TextInput() # added
    zipcode = forms.CharField(max_length=10)
    skills = forms.TextInput()
    git_username = forms.CharField(max_length=200) # added
    years_exp = forms.CharField(max_length=3)
    username =  forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

    class Meta:
        model = CandidateProfile
        fields = ['name', 'bio', 'zipcode', 'skills', 'git_username', 'years_exp', 'username', 'password']

class RecruiterForm(ModelForm):

    name = forms.CharField(max_length=200)
    company = forms.CharField(max_length=300)
    zipcode = forms.CharField(max_length=10)
    username =  forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    
    class Meta:
        model = RecruiterProfile
        fields = ['name', 'company', 'zipcode','username','password']


class PostForm(ModelForm):
    position_title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    position_type = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    location = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    preferred_skills = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    description = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    company = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    expiration_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    status = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    #num_interested = forms.CharField(max_length=100)

    class Meta:
        model = Post
        fields = ['position_title', 'position_type', 'location', 'preferred_skills', 'description', 'company', 'expiration_date', 'status']


