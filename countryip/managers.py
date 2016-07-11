from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from helpers import ip_to_long

class CountryManager(models.Manager):
    def for_ip(self, ip, catch_errors=True):
        if isinstance(ip, basestring):
            try:
                ip = ip_to_long(ip)
            except ValueError:
                pass
        if not isinstance(ip, (int, long)):
            if catch_errors:
                return
            raise TypeError, 'Invalid IP'
        try:
            return self.get_queryset(only_countries=False)\
                       .get(iprange__start__lte=ip, iprange__end__gte=ip)
        except ObjectDoesNotExist:
            if not catch_errors:
                raise

    def get_queryset(self, only_countries=True):
        qs = super(CountryManager, self).get_queryset()
        if only_countries:
            qs = qs.exclude(code='A1').exclude(code='A2')\
                   .exclude(code='X1').exclude(code='X2')
        return qs
