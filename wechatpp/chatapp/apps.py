# Ten kod służy do konfigurowania konfiguracji aplikacji chatapp.

from django.apps import AppConfig #Ten import ładuje klasę App Config z modułu django.apps, który zapewnia klasę bazową dla konfiguracji aplikacji Django.

class ChatappConfig(AppConfig): #definicja nowej klasy chat app Config, która jest podklasą app Config i służy do konfigurowania konfiguracji aplikacji chatapp.
    default_auto_field = 'django.db.models.BigAutoField' #Ten atrybut określa typ pola automatycznego, które będzie używane do tworzenia klucza podstawowego w modelach. Używany jest Big Auto Field odpowiedni dla PostgreSQL.
    name = 'chatapp' #atrybut name określa nazwę aplikacji Django. Używany wewnętrznie przez Django do uzyskiwania dostępu do aplikacji i jej komponentów (adresy URL i szablony).
