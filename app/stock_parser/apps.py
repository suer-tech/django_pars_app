import threading
from django.apps import AppConfig



class ParserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_parser'

    def ready(self):
        from . parser import parsing
        parser_thread = threading.Thread(target=parsing)
        parser_thread.start()
