from django.db import models

class Grupa(models.Model):
    id    = models.AutoField(primary_key=True, auto_created=True)
    naziv = models.CharField(max_length=256)

    def __str__(self):
        return self.naziv


class Vezba(models.Model):
    id      = models.AutoField(primary_key=True, auto_created=True)
    naziv   = models.CharField(max_length=256)
    opis    = models.CharField(max_length=10000)
    grupa   = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.id} - {self.naziv}"
    

class StaKoVezba(models.Model):
    id = models.IntegerField(primary_key=True)
    program_vezbanja = models.IntegerField()


