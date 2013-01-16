from django.core.management.base import BaseCommand, CommandError
from polls.models import Poll

class Command(BaseCommand):
    args = '<poll_id.choice|votes.choice|votes ...>'
    help = 'Imports very unusually formatted list of choices to get around limitations of c9'

    def handle(self, *args, **options):
        
        for arg in args:
            args_list = arg.split('.')
            poll_id = args_list[0]
            self.stdout.write('Poll ID: "%s"' % poll_id)
            choices = args_list[1:]
            try:
                poll = Poll.objects.get(pk=int(poll_id))
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)
            for choice in choices:
                text, votes = choice.split('|')
                c = poll.choice_set.create(choice=text,votes=votes)
                self.stdout.write('\nSuccessfully created choice "%s"' % c.choice)