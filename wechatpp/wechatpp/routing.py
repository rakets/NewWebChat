#kod definiujący wzorce URL do obsługi połączeń WebSocket w kanałach Django.

from django.urls import path, re_path #Importowanie funkcji do definiowania wzorców adresów URL
from .consumers import ChatConsumer   #Import klasy WebSocket Consumer.


websocket_urlpatterns = [                                           #Definiowanie listy wzorców adresów URL dla WebSocket
	path("<room_slug>" , ChatConsumer.as_asgi()) ,                  #Wzorzec URL do obsługi połączeń WebSocket przy użyciu określonej nazwy pokoju
    re_path(r'^ws/(?P<room_slug>[^/]+)/$', ChatConsumer.as_asgi()), #Regularny wzorzec adresu URL dla połączeń WebSocket
]