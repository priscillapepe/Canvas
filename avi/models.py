from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Project:
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to=new_projects)
    description = models.TextField(max_length=200)
    link = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True)
    editor =models.ForeignKey(User,on_delete=on_delete.CASCADE)

def __str__(self):
    return self.title