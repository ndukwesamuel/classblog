from django.contrib.auth.models import  User
from django.db import models
from django.urls import reverse
from  datetime import datetime, date
from django.utils import timezone


class category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

# Create your models here.
class post(models.Model):
    title =models.CharField(max_length=200)
    aurthor = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=255, default='unknown')
    created = models.DateTimeField(editable=False)
    modified= models.DateTimeField()
    likes = models.ManyToManyField(User, related_name= 'blog_post')


    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
            self.modified = timezone.now()
        # ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)
        
        # super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('Blogdetail', args=(str(self.id))) 
        return reverse('home') 


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(post, related_name='comments',  on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        # return reverse('Blogdetail', args=(str(self.id))) 
        return reverse('home') 





