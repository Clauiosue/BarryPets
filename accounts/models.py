from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False, default='DefaultFirstName')
    last_name = models.CharField(max_length=30, blank=False, default='DefaultLastName')
    email = models.EmailField(unique=True, blank=False, default='default@example.com')
    phone = models.CharField(max_length=15, blank=False, default='1234567890')
    address = models.TextField(blank=False, default='Default Address')

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
