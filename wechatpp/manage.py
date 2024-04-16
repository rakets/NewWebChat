#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os   # Importowanie systemu operacyjnego (os) do pracy ze zmiennymi środowiskowymi i wywołaniami systemowymi.
import sys  # Importowanie modułu sys, aby uzyskać dostęp do parametrów i funkcji systemu.


# Definiowanie funkcji main (), która będzie uruchamiać zadania administracyjne.
def main():
    """Run administrative tasks."""
    # Ustawiamy zmienną środowiskową DJANGO_SETTINGS_MODULE dla projektu Django.
    # Ta zmienna określa, którego pliku ustawień projektu użyć .
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wechatpp.settings')

    # Próbuję zaimportować funkcję execute_from_command_line () z modułu django.core.management,
    # który wykonuje polecenia z wiersza poleceń Django.
    try:
        from django.core.management import execute_from_command_line

    # Jeśli wystąpi błąd ImportError, wyświetl komunikat o błędzie i przerwij wykonanie.
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Wykonujemy polecenia z wiersza poleceń Django, przekazując argumenty z sys.argv.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()