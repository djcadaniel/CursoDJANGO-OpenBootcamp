from django.db import models
from datetime import date

class Author(models.Model):
  name= models.CharField(max_length=200)
  email= models.EmailField()
  
  def __str__(self):
    return self.name


class Entry(models.Model):
  author = models.ForeignKey(Author, on_delete= models.CASCADE)
  headLine =  models.CharField(max_length=255)
  bodyText = models.TextField()
  public_date = models.DateField(default=date.today)
  rating = models.IntegerField(default=5)
  
  def __str__(self):
    return self.headLine