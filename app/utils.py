from geopy.distance import geodesic
from flask import jsonify

def calculate_distance_in_miles(lat1,long1,lat2,long2):

    return geodesic((lat1,long1),(lat2,long2)).miles

def serialize_gasStations(gasStations):
    geoJsons = [x.to_geoJson_dict() for x in gasStations]
    feature_collection = {"type": "FeatureCollection", "features": geoJsons}
    return jsonify(feature_collection)

