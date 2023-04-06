from app import app, db
from app.models import GasStation
from app.controller import get_closest_gasStations, get_gas_stations_in_radius
from app.utils import serialize_gasStations
from flask import request


@app.route("/", methods=['GET'])
def get_nearby_gasStations_by_radius():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    rad = request.args.get('rad')
    if not lat or not lng or not rad: return 'arguments are missing'
    gasStations = get_gas_stations_in_radius(
        lng, lat, rad)
    geoJson = serialize_gasStations(gasStations)
    return geoJson


@app.route("/add", methods=["POST"])
def add_gasStation():
    # Get the name, loaction and price from the request form

    name = request.form["name"]
    lat = request.form["lat"]
    lng = request.form["lng"]
    price = request.form["price"]

    # Add a row to the table
    gasStation = GasStation(name=name, lat=lat,
                            lng=lng, price=price)
    db.session.add(gasStation)
    db.session.commit()
    return 'thanks'


@app.route("/gasStations", methods=['GET'])
def get_nearby_gasStations():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    gasStations = get_closest_gasStations(
        lng, lat)
    geoJson = serialize_gasStations(gasStations)
    return geoJson

@app.route('/update/<int:id>', methods=['PATCH'])
def update_gasStation_price(id):
    newPrice = request.form["price"]
    gasStation: GasStation = GasStation.query.get_or_404(id)
    gasStation.price = newPrice
    db.session.commit()
    return 'thanks'
