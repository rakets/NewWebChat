# Ten kod reprezentuje widoki (views) Django, które obsługują żądania użytkowników
# i zwracają odpowiednie odpowiedzi HTTP.

from django.shortcuts import render, get_object_or_404 #Ten import służy do importowania funkcji render i get_object_or_404 z modułu django.shortcuts.
                                                       #Funkcja render służy do wyświetlania szablonów HTML,
                                                       #a get_object_or_404 do pobierania obiektów z bazy danych lub zwracania błędu 404, jeśli obiekt nie zostanie znaleziony.
from .models import Room, Message #importowanie modelow Room i Message

# from django.shortcuts import render


def rooms(request):             #Jest to widok do wyświetlania listy pokoi.
    rooms = Room.objects.all()  #Pobiera wszystkie obiekty Room z bazy danych i przekazuje je do szablonu rooms.html.
    return render(request, "rooms.html", {"rooms": rooms})

def room(request, slug):    #Jest to widok do wyświetlania wiadomości w określonym pokoju. Używa parametru slug do zdefiniowania pokoju,
                            #wyodrębnia odpowiednie wiadomości i przekazuje je do szablonu pokoju.html.
    room_name = Room.objects.get(slug=slug).name
    messages = Message.objects.filter(room=Room.objects.get(slug=slug))

    return render(request, "room.html", {"room_name": room_name, "slug": slug, 'messages': messages})

def chat_1_view(request): #Jest to widok do obsługi żądań dla chat_1/. Wyświetla szablon chat_1_template.html.
    # Логика для обработки запросов для chat_1/
    return render(request, 'chat_1_template.html', {"room_name": "", "slug": ""})