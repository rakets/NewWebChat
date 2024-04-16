#Ten fragment kodu definiuje routing adresów URL dla aplikacji Django.

from django.urls import path #importowanie modułu path z django.urls do tworzenia tras

# Każda trasa określa, który widok (view) Django powinien
# wywołać podczas uzyskiwania dostępu do określonego adresu URL.
from . import views


urlpatterns = [
    path("", views.rooms, name="rooms"),        #Ta trasa odpowiada pustemu ciągowi w adresie URL, co oznacza podstawowy adres URL aplikacji.
                                                # Podczas uzyskiwania dostępu do tego adresu URL zostanie wywołana funkcja pokoje z modułu views
                                                #i zostanie do niej przekazane żądanie. Nazwa trasy jest zdefiniowana jako "rooms".

    path("<str:slug>", views.room, name="room"),  #Ta trasa odpowiada adresom URL zawierającym ciąg znaków (slug).
                                                  #< str:slug> wskazuje Django, że powinien przyjąć ciąg jako argument i przekazać go do funkcji room w views.py.
                                                  #Nazwa trasy jest zdefiniowana jako "room".

    path("chat_1/", views.chat_1_view, name="chat_1"), #Ta trasa odpowiada adresowi URL " chat_1/".
                                                       #Podczas uzyskiwania dostępu do tego adresu URL zostanie wywołana funkcja chat_1_view z modułu views i zostanie do niej przekazane żądanie.
                                                       #Nazwa trasy jest zdefiniowana jako "chat_1".
]

#Trasy te definiują strukturę aplikacji i łączą adresy URL z funkcjami widoków (views),
#które muszą obsługiwać żądania dotyczące tych adresów URL.


