def serialize_gasStations(gasStations):
    geoJsons = [x.to_geoJson_dict() for x in gasStations]
    feature_collection = {"type": "FeatureCollection", "features": geoJsons}
    return feature_collection
