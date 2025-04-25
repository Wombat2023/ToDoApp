from django.shortcuts import render
from .models import Aufgabe


def startseite(request):
    aufgaben = Aufgabe.objects.all()
    return render(request, 'tasks/startseite.html', {'aufgaben': aufgaben})