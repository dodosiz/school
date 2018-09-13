from django.db import models


class ExamCommon(models.Model):
    dictionary = models.CharField(max_length=50)
    speaking = models.CharField(max_length=50)
    listening = models.CharField(max_length=50)
    reading = models.CharField(max_length=50)
    writing = models.CharField(max_length=50)
    grammar = models.CharField(max_length=50)
    test = models.CharField(max_length=50)
    exams = models.CharField(max_length=50)

    class Meta:
        abstract = True


class ExamA(ExamCommon):
    pass


class ExamB(ExamCommon):
    pass
