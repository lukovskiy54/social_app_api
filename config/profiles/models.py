from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserNet(AbstractUser):
    
    GENDER = (
        ('male','male'),
        (
            'female','female'
        )
    )
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='user/avatar/',blank=True,null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=6,choices=GENDER, default='male')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    