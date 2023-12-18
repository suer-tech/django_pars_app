from django.apps import AppConfig


class ParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_parser'

    def ready(self):
        from .management.commands.start_parser import Command
        command_instance = Command()
        command_instance.handle()


