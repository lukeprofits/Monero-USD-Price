import requests


# FUNCTIONS ############################################################################################################
def coingecko(print_price_to_console=False):
    # Make a GET request to the CoinGecko API for XMR/USD exchange rate
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the XMR/USD exchange rate
        xmr_usd_rate = response.json()['monero']['usd']
        print(f"Coin Gecko: {xmr_usd_rate}") if print_price_to_console else None
        return xmr_usd_rate
    else:
        print("Error: Could not retrieve XMR/USD exchange rate")


def binance(print_price_to_console=False):
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'XMRUSDT'})
    #print(response.content)  # Does not work from US ip address
    if response.status_code == 200:
        xmr_usd_rate = float(response.json()['price'])
        print(f'Binance: {xmr_usd_rate}') if print_price_to_console else None
        return xmr_usd_rate
    else:
        return None


def coinmarketcap(print_price_to_console=False):
    response = requests.get('https://coinmarketcap.com/currencies/monero/')
    if response.status_code == 200:
        xmr_usd_rate = round(float(str(response.content).split(
            '"currency":"XMR","currentExchangeRate":{"@type":"UnitPriceSpecification","price":')[1].split(',"')[0]), 2)
        print(f'CoinMarketCap: {xmr_usd_rate}') if print_price_to_console else None
        return xmr_usd_rate
    else:
        return None


def cryptocompare(print_price_to_console=False):
    response = requests.get('https://min-api.cryptocompare.com/data/price', params={'fsym': 'XMR', 'tsyms': 'USD'})
    if response.status_code == 200:
        xmr_usd_rate = response.json()['USD']
        print(f'CryptoCompare: {xmr_usd_rate}') if print_price_to_console else None
        return xmr_usd_rate
    else:
        return None


def kraken(print_price_to_console=False):
    response = requests.get('https://api.kraken.com/0/public/Ticker', params={'pair': 'XMRUSD'})
    if response.status_code == 200:
        xmr_usd_rate = float(response.json()['result']['XXMRZUSD']['c'][0])
        print(f'Kraken: {xmr_usd_rate}') if print_price_to_console else None
        return xmr_usd_rate
    else:
        return None


def bitfinex(print_price_to_console=False):
    response = requests.get('https://api-pub.bitfinex.com/v2/ticker/tXMRUSD')
    if response.status_code == 200:
        xmr_usd_rate = float(response.json()[6])
        print(f'Bitfinex: {xmr_usd_rate}') if print_price_to_console else None
        return xmr_usd_rate
    else:
        return None


def localmonero(print_price_to_console=False):
    # 'nehdddktmhvqklsnkjqcbpmb63htee2iznpcbs5tgzctipxykpj6yrid.onion'
    response = requests.get('https://localmonero.co/buy-monero-with-usd-in-united-states-of-america')
    if response.status_code == 200:
        xmr_usd_rate = float(str(response.content).split(' USD<!-- --> ')[0].split('">')[-1])
        print(f'LocalMonero: {xmr_usd_rate}') if print_price_to_console else None
        return xmr_usd_rate
    else:
        return None


def poloniex(print_price_to_console=False):
    response = requests.get('https://poloniex.com/public?command=returnTicker')
    if response.status_code == 200:
        ticker = response.json().get('USDT_XMR')
        if ticker:
            xmr_usd_rate = float(ticker.get('last'))
            print(f'Poloniex: {xmr_usd_rate}') if print_price_to_console else None
            return xmr_usd_rate
    return None


def huobi(print_price_to_console=False):
    response = requests.get('https://api.huobi.pro/market/detail/merged?symbol=xmrusdt')
    if response.status_code == 200:
        ticker = response.json().get('tick')
        if ticker:
            xmr_usd_rate = float(ticker.get('close'))
            print(f'Huobi: {xmr_usd_rate}') if print_price_to_console else None
            return xmr_usd_rate
    return None


def kucoin(print_price_to_console=False):
    response = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XMR-USDT')
    if response.status_code == 200:
        ticker = response.json().get('data')
        if ticker:
            xmr_usd_rate = float(ticker.get('price'))
            print(f'KuCoin: {xmr_usd_rate}') if print_price_to_console else None
            return xmr_usd_rate
    return None


def hitbtc(print_price_to_console=False):
    response = requests.get('https://api.hitbtc.com/api/3/public/ticker/XMRUSDT')
    if response.status_code == 200:
        ticker = response.json()
        if ticker:
            xmr_usd_rate = round(float(ticker.get('last')), 2)  # round to 2 decimals
            print(f'HitBTC: {xmr_usd_rate}') if print_price_to_console else None
            return xmr_usd_rate
    return None


def get_monero_price_from_all_exchanges(print_price_to_console=False):
    prices = []

    coingecko_price = coingecko(print_price_to_console=print_price_to_console)
    if coingecko_price:
        prices.append(coingecko_price)

    coinmarketcap_price = coinmarketcap(print_price_to_console=print_price_to_console)
    if coinmarketcap_price:
        prices.append(coinmarketcap_price)

    binance_price = binance(print_price_to_console=print_price_to_console)
    if binance_price:
        prices.append(binance_price)

    cryptocompare_price = cryptocompare(print_price_to_console=print_price_to_console)
    if cryptocompare_price:
        prices.append(cryptocompare_price)

    kraken_price = kraken(print_price_to_console=print_price_to_console)
    if kraken_price:
        prices.append(kraken_price)

    bitfinex_price = bitfinex(print_price_to_console=print_price_to_console)
    if bitfinex_price:
        prices.append(bitfinex_price)

    localmonero_price = localmonero(print_price_to_console=print_price_to_console)
    if localmonero_price:
        prices.append(localmonero_price)

    poloniex_price = poloniex(print_price_to_console=print_price_to_console)
    if poloniex_price:
        prices.append(poloniex_price)

    huobi_price = huobi(print_price_to_console=print_price_to_console)
    if huobi_price:
        prices.append(huobi_price)

    kucoin_price = kucoin(print_price_to_console=print_price_to_console)
    if kucoin_price:
        prices.append(kucoin_price)

    hitbtc_price = hitbtc(print_price_to_console=print_price_to_console)
    if hitbtc_price:
        prices.append(hitbtc_price)

    if len(prices) >= 1:  # Make sure that getting at least 1 price was successful
        sorted_prices = sorted(prices)  # low to high
        return sorted_prices
    else:
        print("Error! Didn't get any XMR/USD prices!")
        return None


def average_price(print_price_to_console=False):
    # RECOMMENDED TO USE MEDIAN INSTEAD OF AVERAGE
    sorted_prices = get_monero_price_from_all_exchanges(print_price_to_console=print_price_to_console)
    if sorted_prices:
        # Get average price
        avg_price = sum(sorted_prices) / len(sorted_prices)
        # round to 2 decimals
        avg_price = round(avg_price, 2)
        print(f'\nAverage price is: {avg_price} out of {len(sorted_prices)} exchanges') if print_price_to_console else None
        return avg_price
    else:
        return None


def median_price(print_price_to_console=False):
    sorted_prices = get_monero_price_from_all_exchanges(print_price_to_console=print_price_to_console)
    if sorted_prices:
        # Get median price (less sensitive to outliers than average)
        if len(sorted_prices) % 2 == 1:
            # If the length of the list is odd, return the middle element
            median_price = sorted_prices[len(sorted_prices) // 2]
        else:
            # If the length of the list is even, return the average of the two middle elements
            median_price = (sorted_prices[len(sorted_prices) // 2 - 1] + sorted_prices[len(sorted_prices) // 2]) / 2

        median_price = round(median_price, 2)  # round to 2 decimals

        print(f'\nMedian price is: {median_price} out of {len(sorted_prices)} exchanges') if print_price_to_console else None
        return median_price
    else:
        return None


def print_monero_logo():
    print('''
                    k                                     d                   
                    0Kx                                 dOX                   
                    KMWKx                             dONMN                   
                    KMMMWKx                         dONMMMN                   
                    KMMMMMWKk                     d0NMMMMMN                   
                    KMMMMMMMMXk                 dKWMMMMMMMN                   
                    KMMMMMMMMMMXk             dKWMMMMMMMMMN                   
                    KMMMMMMMMMMMMXk         xKWMMMMMMMMMMMN                   
                    KMMMMMXkNMMMMMMXk     dKWMMMMMW00MMMMMN                   
                    KMMMMM0  xNMMMMMMXk dKWMMMMMWOc dMMMMMN                   
                    KMMMMM0    xNMMMMMMNWMMMMMWOc   dMMMMMN                   
                    KMMMMM0      dXMMMMMMMMMNkc     dMMMMMN                   
                    KMMMMM0        oXMMMMMNx;       dMMMMMN                   
KMMMMMMMMMMMMMMMMMMMMMMMMM0          dNMWk:         dMMMMMMMMMMMMMMMMMMMMMMMMK
KMMMMMMMMMMMMMMMMMMMMMMMMM0            o            dMMMMMMMMMMMMMMMMMMMMMMMMK
KMMMMMMMMMMMMMWNNNNNNNNNNNO                         oNNNNNNNNNNNNMMMMMMMMMMMMO''')
