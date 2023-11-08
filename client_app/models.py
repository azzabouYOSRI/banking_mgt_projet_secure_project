from django.db import models

# Create your models here.
class Client(models.Model):
    cin=models.CharField(max_length=8,primary_key=True)
    name=models.CharField(max_length=100)
    familyName=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phoneNumber=models.Positive(max_length=8)
    
    

    
        
    