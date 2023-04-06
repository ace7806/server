import sqlite3
from dacoPageScrape import scrape


def update_todays_prices():
    data = scrape()
    conn = sqlite3.connect('instance/gas_stations_with_price.sqlite')
    c = conn.cursor()
    for gas_station in data:
        # Update the "price" column for all rows that have a similar "title" value
        c.execute("UPDATE gas_station SET price=? WHERE name LIKE ?",
                  (gas_station['prices']['regular'], '%'+gas_station['name']+'%'))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
