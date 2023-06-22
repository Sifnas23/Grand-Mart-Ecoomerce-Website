from django.db import models

class SignUpdb(models.Model):
    Email = models.EmailField(max_length=20, null=True, blank=True)
    Username = models.CharField(max_length=10, null=True, blank=True)
    Password = models.CharField(max_length=10, null=True, blank=True)
    Confirm = models.CharField(max_length=10, null=True, blank=True)

class Contactdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=20, null=True, blank=True)
    Subject = models.CharField(max_length=20, null=True, blank=True)
    Message = models.TextField(max_length=20, null=True, blank=True)

class Cartdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Total_Price = models.IntegerField(null=True, blank=True)

class Customerdb(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Address = models.TextField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=20, null=True, blank=True)
    State = models.CharField(max_length=20, null=True, blank=True)
    Postalcode = models.IntegerField(null=True, blank=True)
    PhoneNumber = models.IntegerField(null=True, blank=True)
    EmailId = models.EmailField(null=True, blank=True)
