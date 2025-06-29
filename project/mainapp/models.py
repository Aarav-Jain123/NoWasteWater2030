from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    userr = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(default='-', max_length=150)
    name = models.CharField(default='', max_length=150)
    user_points = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.email


class Books(models.Model):
    name =  models.TextField()
    book_id = models.TextField()
    desc =  models.TextField()
    price = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to="media/")
    pdf_link = models.TextField()
    bookss = models.ManyToManyField(UserProfile, related_name='books', blank=True)
    
    def __str__(self):
        return self.name