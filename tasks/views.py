from django.shortcuts import render, redirect, get_object_or_404
from .models import Aufgabe


def startseite(request):
    aufgaben = Aufgabe.objects.all()
    return render(request, 'tasks/startseite.html', {'aufgaben': aufgaben})

def aufgabe_bearbeiten(request, pk):
    aufgabe = get_object_or_404(Aufgabe, pk=pk)
    if request.method == 'POST':
        aufgabe.titel = request.POST['titel']
        aufgabe.beschreibung = request.POST['beschreibung']
        aufgabe.erledigt = request.POST['beschreibung']
        aufgabe.erledigt = 'erledigt' in request.POST
        aufgabe.save()
        return redirect('startseite')
    return render(request, 'tasks/bearbeiten.html', {'aufgabe': aufgabe})

def aufgabe_loeschen(request, pk):
    aufgabe = get_object_or_404(Aufgabe, pk=pk)
    aufgabe.delete()
    return redirect('startseite')
