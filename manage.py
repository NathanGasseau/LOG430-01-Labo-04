#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sgc.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # Injection du jeu d'essai après les migrations si 'runserver' est lancé
    if 'runserver' in sys.argv:
        from django.db import connection
        if connection.introspection.table_names():
            from sgc.core.seed_data import seed
            seed()


if __name__ == '__main__':
    main()
