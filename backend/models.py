# models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator, MaxLengthValidator
def validate_experience_length(value):
    if len(value) > 100:
        raise ValidationError("Experience should not exceed 100 characters.")

class Contact(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    about = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField(blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    def __str__(self):
        return self.name
class Skill(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    name = models.CharField(max_length=100)
    experience = models.CharField(
            max_length=100,
            blank=True,
            null=True,
            validators=[validate_experience_length]
        )
    def __str__(self):
        return self.name
class Service(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title
class Fact(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    title = models.CharField(max_length=100)
    count = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    project = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    technologies = models.CharField(max_length=100)
    url = models.URLField()
    project_date = models.DateField()
    image = models.ImageField(upload_to='photos/')  # For main project image
    description = models.TextField()

    def __str__(self):
        return self.project

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"Image for {self.project.project}"


class Testimony(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    client = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
class Summary(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
class Education(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    acquirement = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    timeline = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
class Experience(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field with auto-increment
    title = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    timeline = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
class Contactme(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

        

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
