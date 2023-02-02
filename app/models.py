from app import db
import json


class GasStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    price = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            "name": self.name,
            "lat": self.lat,
            "lng": self.lng,
            "price": self.price,
        }

    def to_geoJson_dict(self):
        # Create the GeoJSON feature
        feature = {
            'type': 'Feature',
            'properties': {
                'name': self.name,
                'price': self.price
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [self.lng, self.lat]
            }
        }
        return feature

    def to_geoJson(self):
        return json.dumps(self.to_geoJson_dict())
