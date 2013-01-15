from django.core.management.base import BaseCommand, CommandError
from polls.models import Poll
from django.utils import timezone

class Command(BaseCommand):
    args = '<question question ...>'
    help = 'Adds a poll with the specified question(s)'

    def handle(self, *args, **options):
        for question in args:
           
            p = Poll(question=question, pub_date=timezone.now())
            p.save()

            self.stdout.write('Successfully created poll with question "%s"' % p.question )