import requests

from .models import Crypto


def get_symbolPrice_ticker():
    url = "https://fapi.binance.com/fapi/v1/ticker/price"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error occurred while retrieving Kline data:", response.text)
        return None


def get_gainers(sym, gainers, losers):
    api_url = "https://fapi.binance.com/fapi/v1/ticker/24hr"
    # Fetch the top gainers
    params = {
        "symbol": sym,  # Change the symbol to your preferred trading pair
        "sort": "percent_change",
        "limit": 10
    }
    response = requests.get(api_url, params=params)
    item = response.json()
    if float(item['priceChangePercent']) > 0:
        gainers.append(item)
    if float(item['priceChangePercent']) < 0:
        losers.append(item)


def get_top_gainers():
    leaders = []
    api_url = "https://fapi.binance.com/fapi/v1/ticker/24hr"
    # Fetch the top gainers
    params = {
        "symbol": 'BTCUSDT',  # Change the symbol to your preferred trading pair
        "sort": "percent_change",
        "limit": 10
    }
    response = requests.get(api_url, params=params)
    item = response.json()
    leaders.append(item)

    params = {
        "symbol": 'ETHUSDT',  # Change the symbol to your preferred trading pair
        "sort": "percent_change",
        "limit": 10
    }
    response = requests.get(api_url, params=params)
    item = response.json()
    leaders.append(item)
    return leaders

def create_data(item, category):
    crypto = Crypto(ticker=item['symbol'][:-4],
                    category=category,
                    price=item['lastPrice'],
                    change_percent=item['priceChangePercent'],
                    )
    Crypto.save_to_database(crypto)

def get_crypto():
    top = get_top_gainers()

    for t in top:
        create_data(t, 'top')

    index = []
    symb_index = get_symbolPrice_ticker()
    for symb in symb_index:
        if symb['symbol'].endswith('USDT'):
            index.append(symb['symbol'])

    gainers = []
    losers = []

    for x in index:
        get_gainers(x, gainers, losers)

    top_gainers = sorted(gainers, key=lambda x: float(x['priceChangePercent']), reverse=True)[:5]

    for gainer in top_gainers:
        create_data(gainer, 'Лидеры роста')

    top_losers = sorted(losers, key=lambda x: float(x['priceChangePercent']))[:5]

    for loser in top_losers:
        create_data(loser, 'Лидеры падения')
