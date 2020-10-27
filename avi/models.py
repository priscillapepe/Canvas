from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='new_project/')
    description = models.TextField(max_length=200)
    link = models.URLField(max_length=200)
    date = models.DateField(auto_now_add=True)
    editor =models.ForeignKey(User,on_delete=models.CASCADE, default='')

    # def save(self):
    #     super().save()

        
    def __str__(self):
        return self.title