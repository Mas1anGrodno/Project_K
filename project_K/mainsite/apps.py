from django.apps import AppConfig


class MainsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainsite'
    verbose_name = "PROJEKT-K"


    def ready(self):
        import mainsite.signals
