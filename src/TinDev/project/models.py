from django.db import models

# Create your models here.

class UserModelManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    is_recruiter = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500, null=True, blank=True)
    company = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)
    skills = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    experience_years = models.IntegerField(null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(
        max_length=100, unique=True, null=False, blank=False)
    password = models.CharField(max_length=100)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserModelManager()
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def __str__(self):
        return self.username