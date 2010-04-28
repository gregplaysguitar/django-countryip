# data from http://www.maxmind.com/app/csv

from django.db import models
from managers import CountryManager
from helpers import long_to_ip


class Country(models.Model):
    class Meta:
        db_table = 'cc'
        ordering = ['name']

    code = models.CharField(max_length=2, primary_key=True, db_column='cc')
    name = models.CharField(max_length=50, db_column='cn')

    allobjects = models.Manager()
    # `objects` only returns real countries
    objects = CountryManager()

    def __unicode__(self):
        """
        Return the readable version of the name.

        For example, "Moldova, Republic of" will return "Republic of Moldova".
        """
        if ', ' not in self.name:
            return self.name
        bits = self.name.split(', ', 1)
        bits.reverse()
        return ' '.join(bits)


class IPRange(models.Model):
    class Meta:
        db_table = 'ip'

    country = models.ForeignKey(Country, db_column='cc')
    # Note: start and end columns need to be changed to LONG in the database
    # after a syncdb
    start = models.IntegerField(primary_key=True)
    end = models.IntegerField()

    def get_start_ip(self):
        return long_to_ip(self.start)
    start_ip = property(get_start_ip)

    def get_end_ip(self):
        return long_to_ip(self.end)
    end_ip = property(get_end_ip)

    def __unicode__(self):
        return '%s to %s (%s)' % (self.start_ip, self.end_ip, self.country)
