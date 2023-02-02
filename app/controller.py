from app.models import GasStation
from sqlalchemy.sql import text
from app import db
RADIUS_IN_MILES = 3


def get_closest_gasStations(long, lat):
    query_string = f"SELECT *, (6371.0 * ACOS(COS(RADIANS(90 - {lat})) * COS(RADIANS(90 - lat)) + SIN(RADIANS(90 - {lat})) * SIN(RADIANS(90 - lat)) * COS(RADIANS({long} - lng)))) AS distance FROM gas_station ORDER BY distance LIMIT 5"
    gasStations = GasStation.query.from_statement(text(query_string))
    return gasStations


def get_gas_stations_in_radius(lng, lat, radius):
    query_string = text(
        f"SELECT *, (6371.0 * ACOS(COS(RADIANS(90 - {lat})) * COS(RADIANS(90 - lat)) + SIN(RADIANS(90 - {lat})) * SIN(RADIANS(90 - lat)) * COS(RADIANS({lng} - lng)))) AS distance FROM gas_station GROUP BY id HAVING distance < {radius} ORDER BY distance")

    gasStations = GasStation.query.from_statement(
        query_string)
    return gasStations


def get_best_gas_station_near(lat, long):
    gasStations = get_closest_gasStations(lat, long)
    return min(gasStations, key=lambda x: x.price)


def update_price_by_name(name, price):
    gas_stations = GasStation.query.filter(
        GasStation.name.like(f"%{name}%")).all()
    for gas_station in gas_stations:
        gas_station.price = price
    db.session.commit()
