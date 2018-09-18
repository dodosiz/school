from django.db import models
from .exams import ExamA, ExamB
from .pay import Pay1, Pay2, Pay3, Pay4, Pay5, Pay6, Pay7, Pay8, Pay9, Pay10
from .basics import FamilyInfo, FinancialInfo, ContactInfo


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    family = models.OneToOneField(FamilyInfo, blank=True, null=True)
    financial = models.OneToOneField(FinancialInfo, blank=True, null=True)
    contact = models.OneToOneField(ContactInfo, blank=True, null=True)
    exam_a = models.OneToOneField(ExamA, blank=True, null=True)
    exam_b = models.OneToOneField(ExamB, blank=True, null=True)
    pay_1 = models.OneToOneField(Pay1, blank=True, null=True)
    pay_2 = models.OneToOneField(Pay2, blank=True, null=True)
    pay_3 = models.OneToOneField(Pay3, blank=True, null=True)
    pay_4 = models.OneToOneField(Pay4, blank=True, null=True)
    pay_5 = models.OneToOneField(Pay5, blank=True, null=True)
    pay_6 = models.OneToOneField(Pay6, blank=True, null=True)
    pay_7 = models.OneToOneField(Pay7, blank=True, null=True)
    pay_8 = models.OneToOneField(Pay8, blank=True, null=True)
    pay_9 = models.OneToOneField(Pay9, blank=True, null=True)
    pay_10 = models.OneToOneField(Pay10, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def sum_pay(self):
        result = 0.0
        if self.pay_1:
            result += self.pay_1.pay
        if self.pay_2:
            result += self.pay_2.pay
        if self.pay_3:
            result += self.pay_3.pay
        if self.pay_4:
            result += self.pay_4.pay
        if self.pay_5:
            result += self.pay_5.pay
        if self.pay_6:
            result += self.pay_6.pay
        if self.pay_7:
            result += self.pay_7.pay
        if self.pay_8:
            result += self.pay_8.pay
        if self.pay_9:
            result += self.pay_9.pay
        if self.pay_10:
            result += self.pay_10.pay
        return result
