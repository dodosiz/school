from django.db import models


class ExamAbstract(models.Model):
    dictionary = models.CharField(max_length=50, blank=True, null=True)
    speaking = models.CharField(max_length=50, blank=True, null=True)
    listening = models.CharField(max_length=50, blank=True, null=True)
    reading = models.CharField(max_length=50, blank=True, null=True)
    writing = models.CharField(max_length=50, blank=True, null=True)
    grammar = models.CharField(max_length=50, blank=True, null=True)
    test = models.CharField(max_length=50, blank=True, null=True)
    exams = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return 'exams: ' + self.exams


class ExamA(ExamAbstract):
    pass


class ExamB(ExamAbstract):
    pass
