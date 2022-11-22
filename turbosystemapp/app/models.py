from django.db import models
from django.contrib.auth.models import AbstractUser

WORKING_DAYS = [
  ('MONDAY', 'Monday'),
  ('TUESDAY', 'Tuesday'),
  ('WEDNESDAY', 'Wednesday'),
  ('THURSDAY', 'Thursday'),
  ('FRIDAY', 'Friday'),
  ('SATURDAY', 'Saturday'),
  ('SUNDAY', 'Sunday'),
]

class User(AbstractUser):
  is_doctor = models.BooleanField(default=False)
  is_patient = models.BooleanField(default=False)
  dni = models.CharField(max_length=8, help_text='Identification', null=True, blank=True)
  
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

class AppointmentConfiguration(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  working_day = models.CharField(max_length=50, choices=WORKING_DAYS)
  start_time = models.TimeField()
  end_time = models.TimeField()
  
  def __str__(self):
    return self.doctor.get_full_name() + self.day + self.start_time + self.end_time

class Item(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=19, decimal_places=2)
  
  def __str__(self):
    return self.name
  
class Prescription(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  items = models.ManyToManyField(Item, related_name='items')
  
  def __str__(self):
    return self.name

class Diagnostic(models.Model):
  patient = models.ForeignKey(User, on_delete=models.CASCADE)
  description = models.TextField(null=True, blank=True)
  recepient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
  exams = models.ManyToManyField(Exam, related_name='exams')
  prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, blank=True, null=True)

class Patient(models.Model):
  name = models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  birthday = models.DateField(null=True, blank=True)
  dni = models.CharField(max_length=20, null=True, blank=True)
  
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
  