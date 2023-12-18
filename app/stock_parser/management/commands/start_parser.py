import sys
from django.core.management.base import BaseCommand
from stock_parser.parser import parsing

sys.path.append("..")
class Command(BaseCommand):
    help = 'Запуск'

    def handle(self, *args, **options):
        parsing()
        self.stdout.write(self.style.SUCCESS('Задача запущена'))