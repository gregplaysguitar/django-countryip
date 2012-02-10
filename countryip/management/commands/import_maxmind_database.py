from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from countryip.load import load_data



class Command(BaseCommand):
    args = 'csv datafile path'
    
    option_list = BaseCommand.option_list + (
        make_option(
            '--verbose',
            action='store_true',
            dest='verbose',
            default=False,
            help='Verbose mode'
        ),
    )
    
      
    def handle(self, datafile, *args, **options):
        load_data(datafile, options['verbose'])