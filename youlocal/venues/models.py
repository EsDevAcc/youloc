from django.db import models

class Venues(object):
    def __init__(self, id, name, contact, location, categories, distance, verified, stats, url, hours, menu):
        self.id = id
        self.name = name
        self.contact = contact
        self.location = location
        self.categories = categories
        self.distance = distance
        self.verified = verified
        self.stats = stats
        self.url = url
        self.hours = hours
        self.menu = menu
