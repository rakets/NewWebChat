# Ten kod służy do rejestrowania modeli w panelu administracyjnym Django.
# Po dodaniu tego kodu będziemy mogli zarządzać obiektami modeli Room i Message za pośrednictwem panelu administracyjnego Django,
# dodając je, modyfikując i usuwając w razie potrzeby.

from django.contrib import admin #Ten import służy do załadowania modułu admin Django, który zapewnia funkcjonalność panelu administracyjnego.
from .models import Room,Message #Importowanie modelu Room i Message z pliku models.py bieżącej aplikacji.

admin.site.register(Room) #Rejestracja modelu pokoju w Panelu Administracyjnym Django. Po rejestracji model Room będzie dostępny do zarządzania za pośrednictwem interfejsu administracyjnego Django.
admin.site.register(Message) #Rejestracja modelu Message w Panelu Administracyjnym Django

