from django.core.management.base import BaseCommand, CommandError
from polls.models import Poll

class Command(BaseCommand):
    args = ''
    help = 'Shows all polls'

    def handle(self, *args, **options):
        #TODO: add code here to iterate through all polls