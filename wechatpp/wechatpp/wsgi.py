"""
WSGI config for wechatpp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# Importujemy niezbędne moduły do konfiguracji WSGI

# Importujemy system operacyjny (os) do pracy ze zmiennymi środowiskowymi i ustawieniami projektu.
import os

# Importowanie funkcji get_wsgi_application () z modułu django.core.wsgi,
# która inicjuje aplikację WSGI do użytku przez serwer WWW.
from django.core.wsgi import get_wsgi_application

# Ustawienie zmiennej środowiskowa DJANGO_SETTINGS_MODULE dla projektu Django.
# zmienna określa, którego pliku ustawień projektu użyć .
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wechatpp.settings')

# Tworzenie aplikacji WSGI, która będzie używana przez serwer aplikacji.
application = get_wsgi_application()