from django.db import models

# Create your models here.

class feedbacks(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message= models.TextField(max_length=500)
    image= models.ImageField(null=True,blank=True,default='default.png')
    created = models.DateTimeField(auto_now_add=True)
