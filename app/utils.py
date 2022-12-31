from geopy.distance import geodesic
import json
import re

def calculate_distance_in_miles(lat1,long1,lat2,long2):

    return geodesic((lat1,long1),(lat2,long2)).miles

def serialize_geoJsons(features):
    feature_collection = {"type": "FeatureCollection", "features": [features]}
    return feature_collection

