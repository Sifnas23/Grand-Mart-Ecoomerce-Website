from django.db import models

class Category_db(models.Model):
    Name = models.CharField(max_length=20, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)

# class Productdb(models.Model):
#     Category = models.CharField(max_length=20, null=True, blank=True)
#     Product = models.CharField(max_length=20, null=True, blank=True)
#     Price = models.IntegerField(null=True, blank=True)
#     Quantity = models.IntegerField(null=True, blank=True)
#     Description = models.TextField(max_length=100, null=True, blank=True)
#     Image = models.ImageField(upload_to="profile", null=True, blank=True)

class Product_db(models.Model):
    Category = models.CharField(max_length=20, null=True, blank=True)
    Product = models.CharField(max_length=20, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Description = models.TextField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
