from django.db import models


class FamilyInfo(models.Model):
    fathers_name = models.CharField(max_length=255, blank=True)
    mothers_name = models.CharField(max_length=255, blank=True)
    fathers_job = models.CharField(max_length=255, blank=True)
    mothers_job = models.CharField(max_length=255, blank=True)


class FinancialInfo(models.Model):
    afm = models.IntegerField(blank=True)
    fees = models.FloatField(default=0.0)


class ContactInfo(models.Model):
    telephone_1 = models.CharField(max_length=100, blank=True)
    telephone_2 = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)