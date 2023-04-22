# Monero-USD-Price
![Version 1.0](https://img.shields.io/badge/Version-1.0.0-orange.svg)
![Python 3.10.9+](https://img.shields.io/badge/Python-3.10.9+-3776ab.svg)

Monero-USD-Price is an easy way to get the current median or average price of Monero. 

Median is recommended over average, because it is less sensitive to outliers.


# How To Use:
* Install this package: `pip install monero_usd_price`
* Import it at the top of your project: `import monero_usd_price`
* To get the median XMR/USD price: `MoneroUSDPrice.median_price()`
* To get the average XMR/USD price: `MoneroUSDPrice.average_price()`
* To get the XMR/USD price from any of the supported exchanges: `MoneroUSDPrice.coingecko()`, `MoneroUSDPrice.coinmarketcap()`, `MoneroUSDPrice.localmonero()`, etc.

Additonally, you can add the argument `print_price_to_console=True` to any of these if you would like to see output.

For example: `MoneroUSDPrice.median_price(print_price_to_console=True)`, or `MoneroUSDPrice.localmonero(print_price_to_console=True)`


# Donate
If you use this, send me some XMR (even if it's just a few cents)

XMR: `4At3X5rvVypTofgmueN9s9QtrzdRe5BueFrskAZi17BoYbhzysozzoMFB6zWnTKdGC6AxEAbEE5czFR3hbEEJbsm4hCeX2S`


# Supported Exchanges:
* Coingecko
* Binance
* CoinMarketCap
* CryptoCompare
* Kraken
* Bitfinex
* LocalMonero
* Poloniex
* Huobi
* KuCoin
* HitBTC


## Requirements
* [Python 3.10.9](https://www.python.org/downloads/) or above
* [Requests](https://github.com/psf/requests)


## License
[MIT](https://github.com/Equim-chan/vanity-monero/blob/master/LICENSE)
