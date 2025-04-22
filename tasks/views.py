from django.shortcuts import render

def home(request):
    return render(request, 'tasks/home.hmtl')
# Create your views here.
