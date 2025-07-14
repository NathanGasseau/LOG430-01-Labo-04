from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sgc.core'

    def ready(self):
        print(">>> APPLI CORE DÉMARRÉE")