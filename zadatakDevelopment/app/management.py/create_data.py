from django.core.management.base import BaseCommand
from app.models import Data

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data_instance = Data.objects.create(title="Recept-pomocni", description="Ledene kocke – kremasti, osvježavajući kolač djetinjstva koji svi vole. Možda već imate neku svoju varijantu, ali bi ipak trebali isprobati ovaj recept, oduševit ćete se!")
        data_instance.save()
        self.stdout.write(self.style.SUCCESS('Data instance created successfully'))