import configparser
import json
import pytz
from datetime import datetime
from requests import Request, Session
from dateutil import parser

def get_info():
    config = configparser.ConfigParser()
    config.read('coinmarket.ini')
    api_key = config['DEFAULT']['API_KEY']

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = { 'slug': 'bitcoin', 'convert': 'USD' }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    info = json.loads(response.text)

    data = info['data']['1']
    name = data['name']
    symbol = data['symbol']
    total_supply = data['total_supply']
    circulating_supply = data['circulating_supply']
    market_cap = data['quote']['USD']['market_cap']
    price = data['quote']['USD']['price']
    market_cap_dominance = data['quote']['USD']['market_cap_dominance']
    percent_change_1h = data['quote']['USD']['percent_change_1h']
    percent_change_24h = data['quote']['USD']['percent_change_24h']
    volume_24h = data['quote']['USD']['volume_24h']
    volume_change_24h = data['quote']['USD']['volume_change_24h']
    timestamp = info['status']['timestamp']

    timestamp_local = parser.parse(timestamp).astimezone(pytz.timezone('Turkey'))
    formatted_timestamp = timestamp_local.strftime('%Y-%m-%d %H:%M:%S')
    print(f'Name: {name}, Symbol: {symbol}, Price: {price:,.2f}, Percent change (1h): {percent_change_1h}, Percent change (24h): {percent_change_24h}, Total supply: {total_supply}, Circulating supply: {circulating_supply}, Market capitalization: {market_cap}, Market capitalization dominance: {market_cap_dominance}, Volume (24h): {volume_24h}, Volume change (24h): {volume_change_24h}, Timestamp: {formatted_timestamp}')

get_info()