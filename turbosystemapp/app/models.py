from django.db import models

# Create your models here.

class Proceedings(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100, null=True, blank=True)
  date = models.DateField(auto_now=False, auto_now_add=False)
  time = models.TimeField(auto_now=False, auto_now_add=False)
  path = models.CharField(max_length=100)
  status = models.BooleanField(default=True)
  # person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='proceedings')

  def __str__(self):
    return self.title

class Person(models.Model):
  name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  age = models.IntegerField()
  email = models.EmailField()
  phone = models.CharField(max_length=50)
  address = models.CharField(max_length=50)
  proceedings = models.ManyToManyField(Proceedings)

  def __str__(self):
    return self.name