from django.contrib import admin
from django.urls import path
#from django.urls import admin / Wird nicht gebraucht, da Admin nicht aus django.urls kommt sondern aus contrib! 
#from tasks.views import startseite / Wird nicht mehr gebraucht dafür, wird from . import views verwendet!
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.startseite, name='startseite'),
    path('bearbeiten/<int:pk>/', views.aufgabe_bearbeiten, name='aufgabe_bearbeiten'),
    path('loeschen/<int:pk>/', views.aufgabe_loeschen, name='aufgabe_loeschen')
]
