import csv
from django.core.management.base import BaseCommand
from app_ia.models import Laptop

class Command(BaseCommand):
    help = 'Importa dados do arquivo CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        # Caminho do arquivo CSV
        file_path = '/home/fernado/Documentos/archive/laptop_prices.csv'

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                row = {k.strip(): v for k, v in row.items()}
                try:
                    laptop = Laptop(
                        company=row['Company'],
                        product=row['Product'],
                        typename=row['TypeName'],
                        inches=row.get('Inches', None),
                        ram=row.get('Ram', None),
                        os=row['OS'],
                        weight=row.get('Weight', None),
                        price_euros=row['Price_euros'],
                        screen=row['Screen'],
                        screen_width=row.get('ScreenW', None),
                        screen_height=row.get('ScreenH', None),
                        touchscreen=row.get('Touchscreen', None) == 'True',  # Convertendo string para booleano
                        ips_panel=row.get('IPSpanel', None) == 'True',  # Convertendo string para booleano
                        retina_display=row.get('RetinaDisplay', None) == 'True',  # Convertendo string para booleano
                        cpu_company=row['CPU_company'],
                        cpu_freq=row.get('CPU_freq', None),
                        cpu_model=row['CPU_model'],
                        primary_storage=row['PrimaryStorage'],
                        secondary_storage=row.get('SecondaryStorage', None),
                        primary_storage_type=row.get('PrimaryStorageType', None),
                        secondary_storage_type=row.get('SecondaryStorageType', None),
                        gpu_company=row['GPU_company'],
                        gpu_model=row['GPU_model']
                    )
                    laptop.save()
                    self.stdout.write(self.style.SUCCESS(f"Laptop '{laptop.product}' adicionado com sucesso."))
                except KeyError as e:
                    self.stdout.write(self.style.ERROR(f"Erro ao importar linha: {row}. Coluna não encontrada: {e}"))

        self.stdout.write(self.style.SUCCESS("Importação concluída com sucesso."))
