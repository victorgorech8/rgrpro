from django.apps import AppConfig


class SenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.sender'
    verbose_name = 'Рассыльщик'
