from pathlib import Path  #Importowanie klasy Path z modułu Path lib do pracy ze ścieżkami systemu plików.

# Definiowanie katalogu podstawowego projektu.
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

#Tajny klucz Django
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$!(z0fy)6hkx@q9q7u!zvu%3k+3tw=ogfdoptv%3ic&=j!x+*5'

# Tryb debugowania jest włączony.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#Dozwolone hosty dla aplikacji.
ALLOWED_HOSTS = []


#Zainstalowane aplikacje Django
# Application definition
INSTALLED_APPS = [
    'daphne',                       # Aplikacja do pracy z protokołem ASGI.
    'channels',                     # Aplikacja do pracy z żądaniami WebSocket i asynchronicznymi
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatapp',                      # Aplikacja do pracy z czatem.
    
]

# Konfigurowania aplikacji ASGI.
ASGI_APPLICATION = 'wechatpp.asgi.application'

# Konfigurowanie warstw kanałów do pracy z WebSocket.
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer" #Wbudowana warstwa służy do przechowywania wiadomości w pamięci
    }
}

# Warstwy pośrednie do obsługi żądań.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Definiowanie głównego adresu URL konfiguracji.
ROOT_URLCONF = 'wechatpp.urls'

# Przekierowanie po pomyślnym uwierzytelnieniu i wylogowaniu.
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"


# Ustawienia szablonów.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],      # Folder do wyszukiwania szablonów.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Ustawienia aplikacji WSGI.
WSGI_APPLICATION = 'wechatpp.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Ustawienia bazy danych SQLite3.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# Ustawienia sprawdzania haseł użytkowników.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# Ustawienia ustawień międzynarodowych
LANGUAGE_CODE = 'en-us'  # Okreslenie język, który będzie używany w projekcie
TIME_ZONE = 'UTC'        # Ustalenie strefy czasowej
USE_I18N = True          # Jest to ustawienie logiczne, które określa, czy będzie aplikacja korzystać z
                         # internacjonalizacji (i18n) - obsługa różnych języków i lokalizacji wiadomości i formatów daty / godziny
USE_TZ = True            # ustawienie logiczne, określa, czy w projekcie używać stref czasowych.
                         # Po ustawieniu na True Django będzie pracować z datami i godzinami w uniwersalnej strefie czasowej (UTC),
                         #a następnie konwertować je na czas lokalny zgodnie z określoną strefą czasową.


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Ustawienia plików statycznych.
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# Typ pola dla automatycznego pola klucza podstawowego.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'