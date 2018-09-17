from django.db import models


class PayAbstract(models.Model):
    pay = models.FloatField(default=0.0)
    date = models.DateField(blank=True)
    service_number = models.IntegerField(blank=True)

    class Meta:
        abstract = True


class Pay1(PayAbstract):
    pass


class Pay2(PayAbstract):
    pass


class Pay3(PayAbstract):
    pass


class Pay4(PayAbstract):
    pass


class Pay5(PayAbstract):
    pass


class Pay6(PayAbstract):
    pass


class Pay7(PayAbstract):
    pass


class Pay8(PayAbstract):
    pass


class Pay9(PayAbstract):
    pass


class Pay10(PayAbstract):
    pass
