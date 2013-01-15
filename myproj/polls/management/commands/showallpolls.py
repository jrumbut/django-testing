from django.core.management.base import BaseCommand, CommandError
from polls.models import Poll

class Command(BaseCommand):
    args = ''
    help = 'Shows all polls'

    def handle(self, *args, **options):
        polls = Poll.objects.all()
        for poll in polls:
            self.stdout.write('Poll ID = "%s"' % poll.id)
            self.stdout.write('\nPoll question = "%s"' % poll.question)
            self.stdout.write('\nPoll timestampt = "%s"' % poll.pub_date)
            self.stdout.write('\n\n\n')
        
        