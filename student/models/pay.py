from django.db import models
from .student import Student


class Pay(models.Model):
    pay = models.FloatField(default=0.0)
    date = models.DateField(blank=True, null=True)
    service_number = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True, related_name='pays')

    def __str__(self):
        return str(self.pay)
