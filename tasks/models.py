from django.db import models

class Aufgabe(models.Model):
    titel = models.CharField(max_length=200)
    beschreibung = models.TextField()
    erledigt = models.BooleanField(default=False)
    erstellt_am = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.titel
