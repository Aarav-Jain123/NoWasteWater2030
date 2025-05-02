from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_points = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.user.name
    

class Shop(models.Model):
    name =  models.TextField()
    image =  models.ImageField()
    desc =  models.TextField()
    price = models.IntegerField(default=0)
    # type_of_prod = models.TextChoices('theme')
    
    def __str__(self):
        return self.name