import json
import time
import urllib2

FOURSQUARE = "https://api.foursquare.com/v2/venues/explore"
ID = "XPIAKV01P4LNLVNF33P3ECHETOXDYTFPTI43ZPJLWKT31ESY"
SECRET = "0OVXBEHY3CDJHKKG0ENHNQ1ZK0CFNEQVBZ5YRWNO50ZBFAZP"
LAT_LONG = "42.6931325,23.3244314"
VERSION = "20131016"
RADIUS = "20000"

class RequestApi:
    def __init__(self, link=FOURSQUARE, id=ID, secret=SECRET, lat_long=LAT_LONG, version=VERSION, radius=RADIUS):
        self.link = link
        self.id = id
        self.secret = secret
        self.lat_long = lat_long
        self.version = version
        self.radius = str(radius)

    def concat_url(self):
        url = self.link + '?' + \
              'client_id=' + self.id + '&' + \
              'client_secret=' + self.secret + '&' + \
              'll=' + self.lat_long + '&' + \
              'v=' + self.version + '&' + \
              'radius=' + self.radius
        return url

    def validate_field_value(self, item, *names):
        try:
            if len(names) == 2:
                return item[names[0]][names[1]]
            if len(names) == 3:
                return item[names[0]][names[1]][names[2]]
            if len(names) == 4:
                return item[names[0]][names[1]][names[2]][names[3]]
            if len(names) == 5:
                return item[names[0]][names[1]][names[2]][names[3]][names[4]]

            print "echoo"
        except:
            return ''

    def load_json_obj(self, url):

        data = json.load(urllib2.urlopen(url))
        venues = []
        for  ix, item in enumerate (data['response']["groups"][0]['items']):

            all_venues_info = {}
            all_venues_info['id'] = self.validate_field_value(item, 'venue', 'id')  # 1. id
            all_venues_info['name'] = self.validate_field_value(item, 'venue', 'name')  # 2. name

            # all_venues_info = {'id':validate_field_value(item, 'venue', 'id'), 'name':validate_field_value(item, 'venue', 'name')}
            # 3. contact
            all_venues_info['contact'] = {}
            all_venues_info['contact']['twitter'] = self.validate_field_value(item, 'venue', 'contact', 'twitter')
            all_venues_info['contact']['phone'] = self.validate_field_value(item, 'venue', 'contact', 'phone')
            all_venues_info['contact']['formattedPhone'] = self.validate_field_value(item, 'venue', 'contact', 'formattedPhone')

            # 4 categories
            all_venues_info['location'] = {}
            all_venues_info['location']['address'] = self.validate_field_value(item, 'venue', 'location', 'address')
            all_venues_info['location']['crossStreet'] = self.validate_field_value(item, 'venue', 'location', 'crossStreet')
            all_venues_info['location']['city'] = self.validate_field_value(item, 'venue', 'location', 'city')
            all_venues_info['location']['state'] = self.validate_field_value(item, 'venue', 'location', 'state')
            all_venues_info['location']['postalCode'] = self.validate_field_value(item, 'venue', 'location', 'postalCode')
            all_venues_info['location']['country'] = self.validate_field_value(item, 'venue', 'location', 'country')
            all_venues_info['location']['distance'] = self.validate_field_value(item, 'venue', 'location', 'distance')
            all_venues_info['location']['lat'] = self.validate_field_value(item, 'venue', 'location', 'lat')
            all_venues_info['location']['lng'] = self.validate_field_value(item, 'venue', 'location', 'lng')
            all_venues_info['location']['isFuzzed'] = self.validate_field_value(item, 'venue', 'location', 'isFuzzed')

            # 5 categories
            all_venues_info['categories'] = [{
                'id':self.validate_field_value(item, 'venue','categories',0,'id'),
                'name': self.validate_field_value(item, 'venue','categories',0,'name'),
                'pluralName': self.validate_field_value(item, 'venue','categories',0, 'pluralName'),
                'shortName': self.validate_field_value(item, 'venue', 'categories',0, 'shortName'),
                'primary': str(self.validate_field_value(item, 'venue', 'categories', 0, 'primary')),
                'icon':{'prefix':str(item['venue']['categories'][0]['icon']['prefix']),
                        'suffix': str(item['venue']['categories'][0]['icon']['suffix'])}
            }]

            # 6 verified
            all_venues_info['verified'] = str(self.validate_field_value(item, 'venue', 'verified'))

            # 7 rating
            all_venues_info['stats'] = {}
            all_venues_info['stats']['tipCount'] = self.validate_field_value(item, 'venue', 'stats', 'tipCount')
            all_venues_info['stats']['checkinsCount'] = self.validate_field_value(item, 'venue', 'stats', 'checkinsCount')
            all_venues_info['stats']['usersCount'] = self.validate_field_value(item, 'venue', 'stats', 'usersCount')

            # 8 url
            all_venues_info['url'] = self.validate_field_value(item, 'venue', 'url')

            # 8 hours
            all_venues_info['hours'] = {}
            all_venues_info['hours']['status'] = self.validate_field_value(item, 'venue', 'hours', 'status')
            all_venues_info['hours']['isLocalHoliday'] = str(self.validate_field_value(item, 'venue', 'hours', 'isLocalHoliday'))
            all_venues_info['hours']['isOpen'] = str(self.validate_field_value(item, 'venue', 'hours', 'isOpen'))

            #9
            all_venues_info['menu'] = {}
            all_venues_info['menu']['url'] = self.validate_field_value(item, 'venue', 'menu', 'url')
            all_venues_info['menu']['label'] = self.validate_field_value(item, 'venue', 'menu', 'label')
            all_venues_info['menu']['mobileUrl'] = self.validate_field_value(item, 'venue', 'menu', 'mobileUrl')
            all_venues_info['menu']['externalUrl'] = self.validate_field_value(item, 'venue', 'menu', 'externalUrl')
            all_venues_info['menu']['type'] = self.validate_field_value(item, 'venue', 'menu', 'type')
            all_venues_info['menu']['anchor'] = self.validate_field_value(item, 'venue', 'menu', 'anchor')

            #...

            venues.append([all_venues_info])

        return venues


