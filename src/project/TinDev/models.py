from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User #add this
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this


# Create your models here.
class Profile(models.Model):   #add this class and the following fields
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)

    @receiver(post_save, sender=User) #add this
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User) #add this
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

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
    zipcode = models.CharField(max_length=10)
    username =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Name:{self.name}\Company: {self.company}"

class Post(models.Model):
    position_title = models.CharField(max_length=200)
    position_type = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    preferred_skills = models.TextField()
    description = models.TextField()
    company = models.CharField(max_length=200)
    expiration_date = models.DateTimeField('expiration date')
    status = models.CharField(max_length=200)
    num_interested = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.position_title}\n{self.company}\n{self.location}\n{self.description}"
