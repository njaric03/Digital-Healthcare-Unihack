import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps

class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading sample data...'))

        # Get the path to the sample_data directory
        # Iterate over all models in the app
        for model in apps.get_models():
            model_name = model.__name__.lower()
            file_path = os.path.join(settings.SAMPLE_DATA_DIR, f'{model_name}.json')
            print(file_path)
            # Check if the JSON file for the model exists
            if os.path.exists(file_path):
                self.load_data(model, file_path)
            else:
                self.stdout.write(self.style.WARNING(f'JSON file not found for {model_name}. Skipping...'))

        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully.'))

    def load_data(self, model_class, file_path):
        self.stdout.write(f'Loading data for {model_class.__name__}...')
        
        # Read data from the JSON file
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            model_data = json_data.get(model_class.__name__, [])

        # Create instances for each model
        instances = [model_class(**obj) for obj in model_data]

        # Bulk insert into the database
        model_class.objects.bulk_create(instances)
