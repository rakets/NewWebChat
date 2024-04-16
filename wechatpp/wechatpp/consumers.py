# Ten kod definiuje klasę Consumer do obsługi połączeń WebSocket w kanałach Django.

import json                                                   #Importowanie modułu do pracy z JSON.
from channels.generic.websocket import AsyncWebsocketConsumer #Importowanie klasy bazowej do tworzenia asynchronicznych WebSocket-consumers.
from asgiref.sync import sync_to_async                        #Import funkcji dla asynchronicznego owijarki funkcji synchronicznej.

from chatapp.models import Room, Message, User                #Importowanie modeli z aplikacji chatapp


class ChatConsumer(AsyncWebsocketConsumer): #Definicja klasy Chat Consumer dziedziczącej po AsyncWebsocketConsumer.
    async def connect(self):                                            #Metoda wywoływana podczas łączenia klienta z WebSocket.
        self.room_name = self.scope['url_route']['kwargs']['room_slug'] #Pobieranie nazwy pokoju z adresu URL
        self.roomGroupName = 'chat_%s' % self.room_name                 #Tworzenie nazwy grupy dla pokoju.

        #Dodanie bieżącego kanału do grupy WebSocket dla pokoju.
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        #Akceptacja połączenia WebSocket.
        await self.accept()

    #Metoda wywoływana po odłączeniu klienta od WebSocket.
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard( #Usuwanie bieżącego kanału z grupy WebSocket dla pokoju.
            self.roomGroupName,
            self.channel_name
        )

    #Metoda wywoływana po otrzymaniu wiadomości od klienta za pośrednictwem WebSocket.
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)  #Konwertowanie dane tekstowe JSON na obiekt Pythona.
        message = text_data_json["message"]     #Pobieranie wiadomości z JSON.
        username = text_data_json["username"]   #Wyodrębnianie nazwy użytkownika z JSON.
        room_name = text_data_json["room_name"] #Wyodrębnianie nazwy pokoju z JSON

        await self.save_message(message, username, room_name) #Zapisywanie wiadomości w bazie danych.

        #Wysyłanie wiadomości do wszystkich członków grupy WebSocket dla pokoju.
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
                "room_name": room_name,
            }
        )

    #Metoda wysyłania wiadomości do klienta za pośrednictwem WebSocket
    async def sendMessage(self, event):
        message = event["message"]      #Wyodrębnianie wiadomości ze zdarzenia
        username = event["username"]    #Wyodrębnianie nazwy użytkownika ze zdarzenia
        await self.send(text_data=json.dumps({"message": message, "username": username})) #Wysyłanie danych do klienta.

    #Metoda asynchronicznego zapisywania wiadomości w bazie danych
    @sync_to_async
    def save_message(self, message, username, room_name):
        print(username, room_name, "----------------------")           #Wyjście informacji debugowania.
        user = User.objects.get(username=username)                     #Pobieranie obiektu użytkownika z bazy danych.
        room = Room.objects.get(name=room_name)                        #Pobieranie obiektu pokoju z bazy danych.

        Message.objects.create(user=user, room=room, content=message)  #Twórzenie nowego obiektu wiadomości i zapisanie go w bazie danych .



