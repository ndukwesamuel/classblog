from django.contrib.auth.models import  User
from django.db import models
from django.urls import reverse

# Create your models here.
class post(models.Model):
    title =models.CharField(max_length=200)
    aurthor = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('Blogdetail', args=(str(self.id))) 
        return reverse('home') 