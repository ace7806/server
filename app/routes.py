from app import app, db
from app.models import GasStation
from app.controller import get_closest_gasStations, get_closest_gasStations_sql_query
from app.utils import serialize_gasStations
from flask import request,jsonify
@app.route("/")
def index():
    # Select all rows from the table
    return "Hello world"

@app.route("/add", methods=["POST"])
def add_gasStation():
    # Get the name, loaction and price from the request form
    
    name = request.form["name"]
    lat = request.form["lat"]
    long = request.form["long"]
    price = request.form["price"]

    # Add a row to the table
    gasStation = GasStation(name = name, latitude = lat, longitud = long, pricePerLiter = price)
    db.session.add(gasStation)
    db.session.commit()
    return 'thanks'

@app.route("/gasStations",methods=['GET'])
def get_nearby_gasStations():
    # create a custom Response object and pass JSON data and the HTTP status code as arguments
    gasStations = get_closest_gasStations_sql_query(-67.14902119999999,18.3138514)
    geoJson = serialize_gasStations(gasStations)
    return geoJson

@app.route('/update/<int:id>', methods=['PATCH'])
def update_gasStation_price(id):
    newPrice = request.form["price"]
    gasStation : GasStation = GasStation.query.get_or_404(id)
    gasStation.pricePerLiter = newPrice
    
    db.session.commit()
    return 'thanks'


