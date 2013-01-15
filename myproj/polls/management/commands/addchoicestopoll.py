from django.core.management.base import BaseCommand, CommandError
from polls.models import Poll

class Command(BaseCommand):
    args = '<poll_id,choice|votes,choice|votes ...>'
    help = 'Imports very unusually formatted list of choices to get around limitations of c9'

    def handle(self, *args, **options):
        
        args_list = args.split(',"')
        poll_id = args_list[0]
        choices = args_list[1:]
        try:
            poll = Poll.objects.get(pk=int(poll_id))
        except Poll.DoesNotExist:
            raise CommandError('Poll "%s" does not exist' % poll_id)
        for choice in choices:
            text, votes = choice.split('|"')
            
            self.stdout.write('Successfully closed poll "%s"' % poll_id)