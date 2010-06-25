Thanks to smileychris for the original version of this software - see 

http://code.google.com/p/django-countryip/






## Usage

* Put countryip on the pythonpath and add it to your project's installed apps
* Download csv from maxmind - http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip
* Copy GeoIPCountryWhois.csv into the countryip/load directory
* From your project's python prompt, type



    from countryip.load import load_data  
    load\_data()



* In a view, use `Country.objects.for_ip(request.META['REMOTE_ADDR'])` to get country code
* In a template, use `{% load countryip_tags %}` and `{% get_country as country_code %}`


