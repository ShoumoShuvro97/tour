from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=255)
    describtion = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    numberOfPeople = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    country = models.CharField(max_length=255, default='Bangladesh')
    is_visit = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Tourist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    is_visit = models.BooleanField(default=False)
    approved = models.IntegerField(default=0)