from django.db import models
from .basics import FamilyInfo, FinancialInfo, ContactInfo


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    family = models.OneToOneField(FamilyInfo, blank=True, null=True)
    financial = models.OneToOneField(FinancialInfo, blank=True, null=True)
    contact = models.OneToOneField(ContactInfo, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def total_paid(self):
        pays = self.pays.all()
        result = 0.0
        for pay in pays:
            if pay.pay:
                result += pay.pay
        return result

    def total_to_pay(self):
        result = 0.0
        if self.financial.fees:
            result = self.financial.fees - self.total_paid()
        return result
