from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        #return reverse('article-details', args=(str(self.id)))
        return reverse('home')