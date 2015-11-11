from django.db import models

# Create your models here.
class Author(models.Model):
    authorID = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    
class Book(models.Model):
    isbn = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=20)
    authorID = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    publishdate = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

    
