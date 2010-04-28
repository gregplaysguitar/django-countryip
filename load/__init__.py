import csv
from itertools import chain
from os.path import dirname, join
from countryip.models import Country, IPRange

FILENAME = join(dirname(__file__), 'GeoIPCountryWhois.csv')

EXTRA_ROWS = (
    # Private network ranges
    ('10.0.0.0', '10.255.255.255', '167772160', '184549375', 'X1', 'Private Network'),
    ('172.16.0.0', '172.31.255.255', '2886729728', '2887778303', 'X1', 'Private Network'),
    ('192.168.1.1', '192.168.255.255', '3232235520', '3232301055', 'X1', 'Private Network'),
    # Local computer range
    ('127.0.0.0', '127.255.255.255', '2130706432', '2147483647', 'X2', 'Local Computer'),
)

def load_data(filename=None):
    countries = {}
    print 'Opening csv file...'
    filename = filename or FILENAME
    reader = csv.reader(open(filename, "rb"))
    # Delete any existing data
    if Country.allobjects.count() or IPRange.objects.count():
        print 'Deleting existing country ip data...'
        Country.allobjects.all().delete()
        IPRange.objects.all().delete()
    # Load new data
    print 'Loading new country ip data...'
    for row in chain(reader, EXTRA_ROWS):
        try:
            begin_ip, end_ip, begin_num, end_num, country, name = row
        except ValueError:
            continue
        if country not in countries:
            countries[country] = Country.objects.create(code=country, name=name)
        IPRange.objects.create(start=begin_num, end=end_num,
                               country=countries[country])
    print 'Done'
