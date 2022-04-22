from django.db import models

class Ustoz(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    nafaqada = models.BooleanField()
    sana = models.DateField()
    def __str__(self):
        return self.ism

class Fan(models.Model):
    nom = models.CharField(max_length=50)
    yonalish = models.ManyToManyField(Ustoz,on_delete=models.CASCADE)



