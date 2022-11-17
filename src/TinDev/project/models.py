from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_recruiter = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

class Candidate(models.Model)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    zipcode = models.TextField()
    skills = models.CharField(max_length=500)
    years_exp = models.TextField()
    username =  models.CharField(max_length=200)

class Recruiter(models.Model)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=10)