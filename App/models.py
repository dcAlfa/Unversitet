from django.db import models
from django.db.models import DateField


class Ustoz(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    nafaqada = models.BooleanField()
    sana = models.DateField()
    def __str__(self):
        return self.ism


class Fan(models.Model):
    nom = models.CharField(max_length=30)
    cod = models.PositiveSmallIntegerField(default=0)
    vaqt = models.DateField(max_length=30)
    is_active = models.BooleanField()
    def __str__(self):
        return self.nom

class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    fanlar = models.ManyToManyField(Fan)
    ustozlar = models.ManyToManyField(Ustoz)
    def __str__(self):
        return self.nom


