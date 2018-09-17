from django.db import models


class ExamAbstract(models.Model):
    dictionary = models.CharField(max_length=50, blank=True)
    speaking = models.CharField(max_length=50, blank=True)
    listening = models.CharField(max_length=50, blank=True)
    reading = models.CharField(max_length=50, blank=True)
    writing = models.CharField(max_length=50, blank=True)
    grammar = models.CharField(max_length=50, blank=True)
    test = models.CharField(max_length=50, blank=True)
    exams = models.CharField(max_length=50, blank=True)

    class Meta:
        abstract = True


class ExamA(ExamAbstract):
    pass


class ExamB(ExamAbstract):
    pass
