# Monero-USD-Price
![Version 1.4.0](https://img.shields.io/badge/Version-1.4.0-orange.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776ab.svg)

Monero-USD-Price is an easy way to get the current median or average price of Monero in USD.

Median is recommended over average, because it is less sensitive to outliers.


# How To Use:
* Install this package: `pip install monero_usd_price`
* Import it at the top of your project: `import monero_usd_price`
* To get the median XMR/USD price: `monero_usd_price.median_price()`
* To get the average XMR/USD price: `monero_usd_price.average_price()`
* To get the XMR/USD price from any of the supported exchanges: `monero_usd_price.coingecko()`, `monero_usd_price.coinmarketcap()`, `monero_usd_price.localmonero()`, etc.
* To get the amount of Monero that is equivalent to a given amount of USD: `calculate_monero_from_usd(usd_amount)`
* To get the amount of USD that is equivalent to a given amount of Monero: `calculate_usd_from_monero(monero_amount)`
* To convert Monero to Atomic Units: `calculate_atomic_units_from_monero(monero_amount)`
* To convert Atomic Units to Monero: `calculate_monero_from_atomic_units(atomic_units)`

# Donate
If you use this, send me some XMR
- XMR: `4At3X5rvVypTofgmueN9s9QtrzdRe5BueFrskAZi17BoYbhzysozzoMFB6zWnTKdGC6AxEAbEE5czFR3hbEEJbsm4hCeX2S`
- BTC: `1ACCQMwHYUkA1v449DvQ9t6dm3yv1enN87`
- Cash App: `$LukeProfits`
<a href="https://www.buymeacoffee.com/lukeprofits" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;">
</a>


# Supported Exchanges:
* CoinGecko
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
* [Python 3.8](https://www.python.org/downloads/) or above
* [Requests](https://github.com/psf/requests)


## License
[MIT](https://github.com/Equim-chan/vanity-monero/blob/master/LICENSE)
