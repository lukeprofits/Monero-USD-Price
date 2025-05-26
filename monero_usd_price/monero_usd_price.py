import time
from decimal import Decimal
import requests
from contextlib import contextmanager

# FUNCTIONS ############################################################################################################    
def price_request(url, func, pms={}):
    try:
        response = requests.get(url, params=pms)
        if response.status_code == 200:
            usd_rate = func(response.json())
            return Decimal(usd_rate).quantize(Decimal('0.00'))
        else:
            return False
    except:
        return False

def coingecko():
    json_fetch = lambda response: response['monero']['usd']
    return price_request('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd', json_fetch)

def binance():
    json_fetch = lambda response: response['price']
    return price_request('https://api.binance.com/api/v3/ticker/price', json_fetch, {'symbol': 'XMRUSDT'})

#Convert to actually using the API?
# def coinmarketcap(print_price_to_console=False):
#     try:
#         response = requests.get('https://coinmarketcap.com/currencies/monero/')
#         if response.status_code == 200:
#             xmr_usd_rate = Decimal(str(response.content).split(
#                 '"currency":"XMR","currentExchangeRate":{"@type":"UnitPriceSpecification","price":')[1].split(',"')[0]).quantize(Decimal('0.00'))
#             print(f'CoinMarketCap: {xmr_usd_rate}') if print_price_to_console else None
#             return xmr_usd_rate
#         else:
#             return None
#     except:
#         pass


def cryptocompare():
    json_fetch = lambda response: response['USD']
    return price_request('https://min-api.cryptocompare.com/data/price', json_fetch, {'fsym': 'XMR', 'tsyms': 'USD'})

def kraken():
    json_fetch = lambda response: response['result']['XXMRZUSD']['c'][0]
    return price_request('https://api.kraken.com/0/public/Ticker', json_fetch, {'pair': 'XMRUSD'})

def bitfinex():
    json_fetch = lambda response: response[6]
    return price_request('https://api-pub.bitfinex.com/v2/ticker/tXMRUSD', json_fetch, {})

def poloniex():
    json_fetch = lambda response: response.get('USDT_XMR', {}).get('last')
    return price_request('https://poloniex.com/public?command=returnTicker', json_fetch, {})

def huobi():
    json_fetch = lambda response: response.get('tick', {}).get('close')
    return price_request('https://api.huobi.pro/market/detail/merged?symbol=xmrusdt', json_fetch, {})

def kucoin():
    json_fetch = lambda response: response.get('data', {}).get('price')
    return price_request('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XMR-USDT', json_fetch, {})

def hitbtc():
    json_fetch = lambda response: response.get('last')
    return price_request('https://api.hitbtc.com/api/3/public/ticker/XMRUSDT', json_fetch, {})

def get_monero_price_from_all_exchanges_not_threaded():
    prices = []

    exchanges = [coingecko, binance, cryptocompare, kraken, bitfinex, poloniex, huobi, kucoin, hitbtc]
    for exchange in exchanges:
        price = exchange()
        if price:
            prices.append(Decimal(price))
    if len(prices) >= 1:  # Make sure that getting at least 1 price was successful
        sorted_prices = sorted(prices)  # low to high
        return sorted_prices
    else:
        return None


def get_monero_price_from_all_exchanges():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    prices = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(func) for func in [coingecko, binance, cryptocompare, kraken, bitfinex, poloniex, huobi, kucoin, hitbtc]]

        for future in as_completed(futures):
            price = future.result()
            if price:
                prices.append(Decimal(price))

    if len(prices) >= 1:  # Make sure that getting at least 1 price was successful
        sorted_prices = sorted(prices)  # low to high
        return sorted_prices
    else:
        return None


def average_price():
    # RECOMMENDED TO USE MEDIAN INSTEAD OF AVERAGE
    sorted_prices = get_monero_price_from_all_exchanges()
    if sorted_prices:
        # Get average price
        avg_price = sum(sorted_prices) / len(sorted_prices)
        # round to 2 decimals
        avg_price = round(avg_price, 2)
        return avg_price
    else:
        return None


def median_price():
    sorted_prices = get_monero_price_from_all_exchanges()
    if sorted_prices:
        # Get median price (less sensitive to outliers than average)
        if len(sorted_prices) % 2 == 1:
            # If the length of the list is odd, return the middle element
            median_price = sorted_prices[len(sorted_prices) // 2]
        else:
            # If the length of the list is even, return the average of the two middle elements
            median_price = (sorted_prices[len(sorted_prices) // 2 - 1] + sorted_prices[len(sorted_prices) // 2]) / 2

        median_price = round(median_price, 2)  # round to 2 decimals
        return median_price
    else:
        return None


def average_price_not_threaded():
    # RECOMMENDED TO USE MEDIAN INSTEAD OF AVERAGE
    sorted_prices = get_monero_price_from_all_exchanges_not_threaded()
    if sorted_prices:
        # Get average price
        avg_price = sum(sorted_prices) / len(sorted_prices)
        # round to 2 decimals
        avg_price = round(avg_price, 2)
        return avg_price
    else:
        return None


def median_price_not_threaded():
    sorted_prices = get_monero_price_from_all_exchanges_not_threaded()
    if sorted_prices:
        # Get median price (less sensitive to outliers than average)
        if len(sorted_prices) % 2 == 1:
            # If the length of the list is odd, return the middle element
            median_price = sorted_prices[len(sorted_prices) // 2]
        else:
            # If the length of the list is even, return the average of the two middle elements
            median_price = (sorted_prices[len(sorted_prices) // 2 - 1] + sorted_prices[len(sorted_prices) // 2]) / 2

        median_price = round(median_price, 2)  # round to 2 decimals

        return median_price
    else:
        return None


def calculate_monero_from_usd(usd_amount, ):
    monero_price = median_price()
    monero_amount = round(Decimal(usd_amount) / Decimal(monero_price), 12)
    return monero_amount


def calculate_usd_from_monero(monero_amount, ):
    monero_price = median_price()
    usd_amount = round(Decimal(monero_amount) * Decimal(monero_price), 2)
    return usd_amount


def calculate_atomic_units_from_monero(monero_amount):
    atomic_units = int(monero_amount * Decimal(1e12))
    return atomic_units


def calculate_monero_from_atomic_units(atomic_units):
    monero = int(atomic_units) / Decimal(1e12)
    return monero
