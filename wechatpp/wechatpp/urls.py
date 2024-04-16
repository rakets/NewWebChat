"""
URL configuration for Django project

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importujemy niezbędne moduły do pracy z adresami URL i interfejsem administracyjnym Django
from django.contrib import admin
from django.urls import path, include

# Definiowanie urlpatterns, który zawiera wzorce adresów URL dla projektu

# URL, aby uzyskać dostęp do panelu administracyjnego Django
urlpatterns = [
    path('admin/', admin.site.urls),                        # URL umożliwiający dostęp do panelu administracyjnego pod adresem / admin/

    path("accounts/", include("django.contrib.auth.urls")), # Adresy URL dla Wbudowanych widoków uwierzytelniania Django
                                                            # Zawiera adresy URL logowania, wylogowywania, resetowania hasła i innych funkcji uwierzytelniania

    path('',include('chatapp.urls')),                       # Włączenie adresy URL z aplikacji whatsapp
                                                            # Umożliwia obsługę niestandardowych adresów URL związanych z funkcjonalnością aplikacji
]