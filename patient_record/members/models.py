from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    blood_group = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    volume_of_blood_donated = models.CharField(max_length=255)
