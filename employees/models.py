from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_no = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100)
    short_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profiles/' , default='profiles/default.jpg')


    def __str__(self):
        return f'{self.name} - {self.designation}'

