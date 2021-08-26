from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    staff = models.IntegerField()
    is_active = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)


class Office(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    country = CountryField()
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)


class UserToCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)


class Cooperation(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=250, blank=True, null=True)
    company = models.ManyToManyField(Company)
    is_active = models.BooleanField(default=True)
    last_update = models.DateTimeField(auto_now=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)

# class CompanyToCooperation(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.PROTECT)
#     cooperation = models.ForeignKey(Cooperation, on_delete=models.PROTECT)
