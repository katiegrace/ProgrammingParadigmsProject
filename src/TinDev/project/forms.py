'''
from django import forms
from project.models import UserModel

class CandidateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    name = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(max_length=5, required=True)
    skills = forms.CharField(max_length=500, required=True)
    experience_years = forms.IntegerField(required=True)
    username = forms.CharField(max_length=100, required=True)

    class Meta:
        model = UserModel
        fields = ['name', 'bio', 'zip_code', 'skills', 'github',
                  'experience_years', 'education', 'username', 'password']

class RecruiterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    name = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(max_length=5, required=True)
    username = forms.CharField(max_length=100, required=True)
    

    class Meta:
        model = UserModel
        fields = ['name', 'company', 'zip_code', 'username', 'password']


class Login(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
'''

from django.forms import ModelForm
from django import forms
from .models import CandidateProfile
from .models import RecruiterProfile

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