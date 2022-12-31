from app import db
import json
class GasStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitud = db.Column(db.Float)
    pricePerLiter = db.Column(db.Float)

    def to_dict(self):
        return {
            'id':self.id,
            "name":self.name,
            "latitude":self.latitude,
            "longitud":self.longitud,
            "pricePerLiter":self.pricePerLiter,
        }

    def serialize_gas_stations(gasStations):
        return [x.to_dict() for x in gasStations]

    def to_geojson(self):
        # Create the GeoJSON feature
        feature = {
            'type': 'Feature',
            'properties': {
                'name': self.name,
                'pricePerLiter': self.pricePerLiter
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [self.longitud, self.latitude]
            }
        }
        # Convert the feature to a JSON string and return it
        return json.dumps(feature)


    