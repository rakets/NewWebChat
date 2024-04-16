#Ten kod służy do konfigurowania routingu i protokołów w Django Channels, który umożliwia pracę z WebSockets i innymi protokołami asynchronicznymi w Django.

import os                                          #Importowanie modułu do pracy ze zmiennymi środowiskowymi
from django.core.asgi import get_asgi_application  #Importowanie funkcji w celu uzyskania obiektu aplikacji WSGI Django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wechatpp.settings') #Ustawienie zmiennej środowiskowej DJANGO_SETTINGS_MODULE dla aplikacji Django.

from channels.auth import AuthMiddlewareStack               #Import middleware do uwierzytelniania WebSocket.
from channels.routing import ProtocolTypeRouter, URLRouter  #Importuj klasę, aby skonfigurować routing WebSocket i inne protokoły.
from . import routing                                       #importowanie modułu z trasami WebSocket.

application = ProtocolTypeRouter(            #Konfigurowanie obiektu Protocol Type Router w celu określenia sposobu obsługi różnych typów żądań.
    {
        "http": get_asgi_application(),      #W przypadku żądań HTTP używana jest standardowa aplikacja Django.
        "websocket": AuthMiddlewareStack(    #W przypadku żądań WebSocket używane jest oprogramowanie pośrednie do uwierzytelniania.
            URLRouter(
                routing.websocket_urlpatterns #Żądania są kierowane przez adres URL Router z określonymi trasami
            )
        )
    }
)