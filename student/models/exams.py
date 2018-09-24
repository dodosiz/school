from django.db import models
from .student import Student
import re


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

    def average(self):
        counter = 0
        result = 0
        if re.findall(r'-?\d+\.?\d*', self.dictionary):
            result += float(re.findall(r'-?\d+\.?\d*', self.dictionary)[0])
            counter += 1
        if re.findall(r'-?\d+\.?\d*', self.speaking):
            result += float(re.findall(r'-?\d+\.?\d*', self.speaking)[0])
            counter += 1
        if re.findall(r'-?\d+\.?\d*', self.listening):
            result += float(re.findall(r'-?\d+\.?\d*', self.listening)[0])
            counter += 1
        if re.findall(r'-?\d+\.?\d*', self.reading):
            result += float(re.findall(r'-?\d+\.?\d*', self.reading)[0])
            counter += 1
        if re.findall(r'-?\d+\.?\d*', self.writing):
            result += float(re.findall(r'-?\d+\.?\d*', self.writing)[0])
            counter += 1
        if re.findall(r'-?\d+\.?\d*', self.grammar):
            result += float(re.findall(r'-?\d+\.?\d*', self.grammar)[0])
            counter += 1
        if re.findall(r'-?\d+\.?\d*', self.test):
            result += float(re.findall(r'-?\d+\.?\d*', self.test)[0])
            counter += 1
        if re.findall(r'-?\d+\.?\d*', self.exams):
            result += float(re.findall(r'-?\d+\.?\d*', self.exams)[0])
            counter += 1
        if counter > 0:
            return result/counter
        else:
            return '-'


"""
import re
[float(s) for s in re.search(r'-?\d+\.?\d*', 'he33.45llo -42 I\'m a 32 string 30')]
"""
