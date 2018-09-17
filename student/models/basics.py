from django.db import models


class FamilyInfo(models.Model):
    fathers_name = models.CharField(max_length=255, blank=True, null=True)
    mothers_name = models.CharField(max_length=255, blank=True, null=True)
    fathers_job = models.CharField(max_length=255, blank=True, null=True)
    mothers_job = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.fathers_name + ' and ' + self.mothers_name


class FinancialInfo(models.Model):
    afm = models.IntegerField(blank=True, null=True)
    fees = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.fees)


class ContactInfo(models.Model):
    telephone_1 = models.CharField(max_length=100, blank=True, null=True)
    telephone_2 = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.telephone_1
