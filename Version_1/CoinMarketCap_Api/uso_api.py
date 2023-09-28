import requests

def get_historical_data(symbol, convert, start, end):
  ENDPOINT = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical"
  API_KEY = "la tua chiave API"
  PARAMETERS = {
    "symbol": symbol,
    "convert": convert,
    "time_start": start,
    "time_end": end
  }
  HEADERS = {
    "Accept": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
  }
  response = requests.get(ENDPOINT, params=PARAMETERS, headers=HEADERS)
  return response.json()


if __name__ == "__main__":
  data = get_historical_data("BTC", "USD", "2023-01-03T00:00:00.000Z", "2023-01-04T12:50:00.000Z")
  print(data)
