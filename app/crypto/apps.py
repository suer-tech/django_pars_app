import threading
from django.apps import AppConfig


class CryptoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crypto'


    def ready(self):
        from . crypto_price import get_crypto
        crypto_thread = threading.Thread(target=get_crypto)
        crypto_thread.start()
