import requests
from bs4 import BeautifulSoup


def scrape():
    url = 'https://www.daco.pr.gov/recursos/estudios-economicos/datos-de-combustible/'
    response = requests.get(url)
    html = response.text

    # serialize gas station to a dict

    def to_dict(name, regular_gas_price, premium_gas_price, diesel_gas_price):
        return {'name': name, 'prices':
                {
                    'regular': regular_gas_price,
                    'premium': premium_gas_price,
                    'diesel': diesel_gas_price
                }
                }

    soup = BeautifulSoup(html, 'html.parser')
    # gets all the card elements in the html
    # that holds all the gas stations with their prices
    elements = soup.select('.cus_datos2')
    output = []
    seen = set()
    for element in elements:
        # extract the name and cleans the text
        names = element.find('h3').text.strip().split('/')
        # get all the list elements in which contains the gas prices
        gas_prices = element.find_all('li')
        regular_gas_price = gas_prices[0].text.removesuffix('Regular')
        premium_gas_price = gas_prices[1].text.removesuffix('Premium')
        diesel_gas_price = gas_prices[2].text.removesuffix('Diésel')
        for name in names:
            name = name.strip()
            if name not in seen:
                seen.add(name)
                gas_station = to_dict(name, regular_gas_price,
                                      premium_gas_price, diesel_gas_price)
                print(gas_station)
                output.append(gas_station)
    return output
    # save as a json file
    # with open('scripts/gasStationPrices.json', 'w') as f:
    #     json.dump(output, f)
