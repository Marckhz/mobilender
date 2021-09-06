from django.apps import AppConfig

class MobilenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobilender'
    
    def ready(self):
        import mobilender.signals
