from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=34)
    password = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    
   