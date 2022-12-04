from django.db import models

# Create your models here.

class CandidateProfile(models.Model):

    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=300) # added
    zipcode = models.CharField(max_length=10)
    skills = models.CharField(max_length=300)
    git_username = models.CharField(max_length=200) # added
    years_exp = models.CharField(max_length=3)
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class RecruiterProfile(models.Model):

    name = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=10)
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Post(models.Model):
    position_title = models.CharField(max_length=200)
    position_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    preferred_skills = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    company = models.CharField(max_length=200)
    expiration_date = models.DateTimeField()
    status = models.CharField(max_length=200)
    #num_interested = models.CharField(max_length=100)
    recruiter= models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, default="")
    #def __str__(self):
        #return self.title

class Offer(models.Model):
    recruiterOff = models.ForeignKey(RecruiterProfile, on_delete=models.CASCADE, default="")
    candidateOff = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, default="")
    salary_info = models.CharField(max_length=200)
    due_date = models.DateTimeField()