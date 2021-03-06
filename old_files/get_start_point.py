'''
Software Design Final Project: Trail Blazer

get_start_point.py finds a starting location from a user specified point on a google map embedded on profile.html to return a lattitude and longitude starting coordinate.
'''
import googlemaps
from datetime import datetime
from googlemaps import convert


import os

GMAP_BASE_URL = "https://www.google.com/maps/embed/v1/place?key="

DIRECTIONS_API_KEY = os.environ["DIRECTIONS_KEY"]
GEOCODING_API_KEY = os.environ['GEOCODING_KEY']


gmaps = googlemaps.Client(key=GEOCODING_API_KEY)


def format_location(location):
    return location.replace(" ","+")
