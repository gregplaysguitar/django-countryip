## Usage

* Put countryip on the pythonpath and add it to your project's installed apps
* Download csv from maxmind - http://geolite.maxmind.com/download/geoip/database/GeoIPCountryCSV.zip
* Copy GeoIPCountryWhois.csv into the countryip/load directory
* From your project's python prompt, type

      from countryip.load import load_data
      load\_data()



