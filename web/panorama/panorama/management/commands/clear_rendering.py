from django.core.management import BaseCommand
from datasets.panoramas.models import Panorama


class Command(BaseCommand):
    def handle(self, *args, **options):
        Panorama.rendering.update(status=Panorama.STATUS.to_be_rendered)
