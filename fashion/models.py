from django.db import models

# Create your models here.
class fashion(models.Model):
    name=models.CharField(max_length=50)
    product=models.CharField(max_length=50)
    
