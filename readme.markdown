Thanks to smileychris for the original version of this software - see 

http://code.google.com/p/django-countryip/






## Usage

* Put countryip on the pythonpath and add it to your project's installed apps
* Download and unzip csv from maxmind - http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip
* From your project's home directory, type


    python manage.py import\_maxmind\_database path/to/GeoIPCountryWhois.csv


* In a view, use `Country.objects.for_ip(request.META['REMOTE_ADDR'])` to get country code
* In a template, use `{% load countryip_tags %}` and `{% get_country as country_code %}`


