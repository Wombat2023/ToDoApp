from django.contrib import admin
from django.urls import path
#from django.urls import admin / Wird nicht gebraucht, da Admin nicht aus django.urls kommt sondern aus contrib! 
from tasks.views import startseite

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.startseite, name='startseite'),
]
