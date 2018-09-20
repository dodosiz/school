from django.db import models
from .student import Student


class Exam(models.Model):
    dictionary = models.CharField(max_length=50, blank=True, null=True)
    speaking = models.CharField(max_length=50, blank=True, null=True)
    listening = models.CharField(max_length=50, blank=True, null=True)
    reading = models.CharField(max_length=50, blank=True, null=True)
    writing = models.CharField(max_length=50, blank=True, null=True)
    grammar = models.CharField(max_length=50, blank=True, null=True)
    test = models.CharField(max_length=50, blank=True, null=True)
    exams = models.CharField(max_length=50, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True, related_name='exams')

    def __str__(self):
        return 'exams: ' + self.exams
