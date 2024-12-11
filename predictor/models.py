from django.db import models

# Create your models here.
class Document(models.Model):
    file = models.FileField(upload_to='file/')

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title