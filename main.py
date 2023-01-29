import requests

def get_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return price

price = get_price()
print("The current price of Bitcoin is: $" + price)
