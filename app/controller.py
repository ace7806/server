from app.models import GasStation
from app import db
from app.utils import calculate_distance_in_miles, serialize_gasStations
import heapq
from sqlalchemy.sql import text

RADIUS_IN_MILES = 3

def get_closest_gasStations_sql_query(long,lat):
    query_string = f"SELECT *, (6371.0 * ACOS(COS(RADIANS(90 - {lat})) * COS(RADIANS(90 - latitude)) + SIN(RADIANS(90 - {lat})) * SIN(RADIANS(90 - latitude)) * COS(RADIANS({long} - longitud)))) AS distance FROM gas_station ORDER BY distance LIMIT 5"
    gasStations = GasStation.query.from_statement(text(query_string))
    return gasStations

def get_closest_gasStations(lat,long):
    #TODO: optimize code. Im thinking i can do lines 10 to 16 with a sort one liner or do calcuations when doing the query     

    #get all the Gas Stations from the database
    gasStations = GasStation.query.all()

    #sort based on distance from point
    mq= []
    for x in gasStations:
        heapq.heappush(mq,(calculate_distance_in_miles(lat,long,x.latitude,x.longitud), x))
    #extract the gas stations from minHeap
    size = min(5,len(mq))
    gasStations = [heapq.heappop(mq)[1] for x in range(size)]
    for x in gasStations:print(x.name)
    return gasStations

def get_best_gas_station_near(lat,long):
    gasStations = get_closest_gasStations(lat,long)
    return min(gasStations, key = lambda x: x.pricePerLiter)

