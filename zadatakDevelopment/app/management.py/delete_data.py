from django.core.management.base import BaseCommand
from app.models import Data

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Data.objects.filter(title__startswith="Recept-pomocni").delete()

        self.stdout.write(self.style.SUCCESS('Data deleted successfully'))