from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from project.models import User, Candidate, Recruiter

class CandidateSignUpForm(UserCreationForm):
    #this form automatically sets a username and password 
    name = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(max_length=5, required=True)
    skills = forms.CharField(max_length=500, required=True)
    experience_years = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_candidate = True
        user.save()
        candidate = Candidate.objects.create(user=user)
        return user

class RecruiterSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_recruiter = True
        if commit:
            user.save()
        return user