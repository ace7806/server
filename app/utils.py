from geopy.distance import geodesic


def calculate_distance_in_miles(lat1, long1, lat2, long2):
    return geodesic((lat1, long1), (lat2, long2)).miles


def serialize_gasStations(gasStations):
    geoJsons = [x.to_geoJson_dict() for x in gasStations]
    feature_collection = {"type": "FeatureCollection", "features": geoJsons}
    return feature_collection
