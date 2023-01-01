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

    def to_geoJson_dict(self):
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
        return feature

    def to_geoJson(self):
        return json.dumps(self.to_geoJson_dict())


    