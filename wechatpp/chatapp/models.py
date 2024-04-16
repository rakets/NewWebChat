#Ten kod definiuje modele Django dla aplikacji czatu (Room i Message), które będą
#używane do przechowywania informacji o pokojach czatu i wiadomościach wysyłanych do tych pokoi.

from django.db import models          #Ten import zapewnia dostęp do klas i funkcji zdefiniowanych w module models Django.
                                      # Moduł models zawiera klasy bazowe do definiowania modeli bazy danych, takich jak Models,
                                      #ForeignKey, CharField i wiele innych. Służy do tworzenia struktury danych aplikacji, która ma być wyświetlana w bazie danych.

from django.contrib.auth.models import User #Ten import umożliwia użycie modelu User dostarczonego przez Django do uwierzytelniania użytkowników.
                                            #Model użytkownika zawiera podstawowe informacje o użytkowniku, takie jak imię i nazwisko, adres e-mail i hasło.

class Room(models.Model):                   #Definiowanie modelu pokoju, który będzie przechowywać informacje o pokojach czatu.
    name = models.CharField(max_length=20)  #Pole name typu CharField to nazwa pokoju, ma maksymalną długość 20 znaków.
    slug = models.SlugField(max_length=100) #Pole slug typu SlugField służy do tworzenia unikalnego adresu URL pokoju i ma maksymalną długość 100 znaków.
    def __str__(self):                                          #Metoda__ str _ _ zwraca ciąg znaków reprezentujący obiekt pokoju.
        return "Room : " + self.name + " | Id : " + self.slug   #Zwraca ciąg zawierający nazwę pokoju i jego identyfikator (slug).

class Message(models.Model):                                 #Definiuje Model Message, który będzie przechowywać informacje o wiadomościach wysyłanych do pokojów czatowych.
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Klucz obcy user, który odwołuje się do modelu użytkownika Django (User). Po usunięciu użytkownika posty zostaną również usunięte (on_delete=models.CASCADE).
    content = models.TextField()  #Pole content typu TextField przechowuje tekst wiadomości.
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #Klucz obcy room odwołuje się do modelu Room. Po usunięciu pokoju wiadomości zostaną również usunięte (on_delete=models.CASCADE).
    created_on = models.DateTimeField(auto_now_add=True) #Pole created_on typu DateTimeField przechowuje datę i godzinę utworzenia wiadomości.
                                                         #auto_now_add=True określa, że pole zostanie automatycznie wypełnione bieżącą datą i godziną podczas tworzenia rekordu.
    def __str__(self): #Metoda zwraca ciąg znaków reprezentujący obiekt wiadomości.
        return "Message is :- " + self.content #Zwraca ciąg zawierający tekst wiadomości.
