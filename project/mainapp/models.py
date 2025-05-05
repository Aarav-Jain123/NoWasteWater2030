from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Themes(models.Model):
    name =  models.TextField()
    image =  models.ImageField()
    desc =  models.TextField()
    price = models.IntegerField(default=0)
    styles = models.TextField()
    
    def __str__(self):
        return self.name


class Logos(models.Model):
    name =  models.TextField()
    image =  models.ImageField()
    desc =  models.TextField(default='Should be of max resolution 150x150 pixels')
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    userr = models.OneToOneField(User, on_delete=models.CASCADE)
    user_points = models.IntegerField(default=0)
    themess = models.ManyToManyField(Themes, related_name='themes', blank=True)
    logoss = models.ManyToManyField(Logos, related_name='logos', blank=True)
    
    
    def __str__(self):
        return self.user.name