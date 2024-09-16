from django.db import models
from employees.models import Employees

# Create your models here.
class Profiles(models.Model):
    user = models.OneToOneField(Employees, on_delete=models.CASCADE)
    bg_image = models.ImageField(upload_to='bg_image/')
    profile_image = models.ImageField(upload_to='profiles/')
