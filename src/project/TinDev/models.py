from django.db import models
#hi

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    zipcode = models.TextField()
    skills = models.CharField(max_length=500)
    git_username = models.CharField(max_length=200)
    years_exp = models.TextField()
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f"Name:{self.name}\nBio: {self.bio}"

class Recruiter(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    zipcode = models.TextField()
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Name:{self.name}\Company: {self.company}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.title} by {self.author_name} ({self.pub_date})"
