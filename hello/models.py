from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField (max_length=255)
    email = models.EmailField ()
    message = models.TextField ()
    date = models.DateTimeField (auto_now_add=True)
    def __str__(self):
        return self.name 
class student (models.Model) : 
    rollno = models.CharField(max_length=20 , unique=True) # Added new fields
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=500)
    def __str__(self):
        return self.name
  
    