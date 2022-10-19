from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  is_doctor = models.BooleanField(default=False)
  is_patient = models.BooleanField(default=False)
  
  def __str__(self):
    return self.username + ' ' + self.email
  

class Disease(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
class Exam(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  file = models.FileField(upload_to='exams', null=True, blank=True)
  diseases = models.ManyToManyField(Disease, related_name='diseases')
  
  def __str__(self):
    return self.name

class Address(models.Model):
  street = models.CharField(max_length=250)
  number = models.IntegerField(null = True, blank = True)
  complement = models.CharField(max_length=50, blank=True, null=True)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  state = models.CharField(max_length=150)
  neighborhood = models.CharField(max_length=50)
  
  def __str__(self):
    return self.street + self.number + self.complement
  
class Doctor(models.Model):
  name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  birthday = models.DateField()
  address = models.ForeignKey(Address, on_delete=models.CASCADE)
  degree = models.CharField(max_length=50)
  degree_file = models.FileField(upload_to='degree_files', null=True, blank=True)
  
  def __str__(self):
    return self.name
  
  def get_full_name(self):
    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()

class Patient(models.Model):
  name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  birthday = models.DateField(null=True, blank=True)
  disease = models.ManyToManyField(Disease)
  exams = models.ManyToManyField(Exam, related_name='exams')
  
  def __str__(self):
    return self.name
  
  def get_full_name(self):
    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()
  
class Appointment(models.Model):
  date = models.DateTimeField()
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.date + self.doctor.get_full_name() + self.patient.get_full_name()