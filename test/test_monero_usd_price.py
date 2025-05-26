from unittest import TestCase, mock
from monero_usd_price.monero_usd_price import coingecko, binance, cryptocompare, kraken, bitfinex,\
    poloniex, huobi, kucoin, hitbtc, get_monero_price_from_all_exchanges, get_monero_price_from_all_exchanges_not_threaded,\
    average_price, average_price_not_threaded, median_price, median_price_not_threaded, calculate_monero_from_usd,\
    calculate_usd_from_monero, calculate_atomic_units_from_monero, calculate_monero_from_atomic_units
from decimal import Decimal
import requests_mock
from contextlib import contextmanager

class TestMoneroUsdPrice(TestCase):
    def coingecko_request(self, mock):
        return mock.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd', json={'monero': {'usd': 398.17}})

    def binance_request(self, mock):
        return mock.get('https://api.binance.com/api/v3/ticker/price?symbol=XMRUSDT', json={'price': '200.00'})

    # def coinmarketcap_request(self, mock):
    #     return mock.get('https://coinmarketcap.com/currencies/monero/', json=[{'price_usd': '398.17'}])

    def cryptocompare_request(self, mock):
        return mock.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD', json={'USD': '398.17'})

    def kraken_request(self, mock):
        return mock.get('https://api.kraken.com/0/public/Ticker?pair=XMRUSD', json={'result': {'XXMRZUSD': {'c': ['200.00', '10000']}}})

    def bitfinex_request(self, mock):
        return mock.get('https://api-pub.bitfinex.com/v2/ticker/tXMRUSD', json=[0, 1, 2, 3, 4, 5, 200.00, 7, 8])

    def poloniex_request(self, mock):
        return mock.get('https://poloniex.com/public?command=returnTicker', json={'USDT_XMR': {'last': '0.2'}})

    def huobi_request(self, mock):
        return mock.get('https://api.huobi.pro/market/detail/merged?symbol=xmrusdt', json={'tick': {'close': '200.00'}})

    def kucoin_request(self, mock):
        return mock.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=XMR-USDT', json={'data': {'price': '250.00'}})

    def hitbtc_request(self, mock):
        return mock.get('https://api.hitbtc.com/api/3/public/ticker/XMRUSDT', json={'last': '200.00'})

    def failed_coingecko_request(self, mock):
        return mock.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd', status_code=401)

    @contextmanager
    def mock_requests_even(self):
        with requests_mock.Mocker() as m:
            self.coingecko_request(m)
            self.cryptocompare_request(m)
            self.binance_request(m)
            self.kraken_request(m)
            self.bitfinex_request(m)
            self.poloniex_request(m)
            self.huobi_request(m)
            self.kucoin_request(m)
            yield m

    @contextmanager
    def mock_requests_odd(self):
        with requests_mock.Mocker() as m:
            self.coingecko_request(m)
            self.cryptocompare_request(m)
            self.binance_request(m)
            self.kraken_request(m)
            self.bitfinex_request(m)
            self.poloniex_request(m)
            self.huobi_request(m)
            self.kucoin_request(m)
            self.hitbtc_request(m)
            yield m

    def test_median_price(self):
        with self.mock_requests_odd():
            self.assertEqual(median_price(), Decimal('200.00'))

        with self.mock_requests_even():
            self.assertEqual(median_price(), Decimal('200.00'))

    def test_median_price_failure(self):
        with mock.patch('monero_usd_price.monero_usd_price.price_request', return_value=False): 
            self.assertEqual(median_price(), None)

    def test_get_monero_price_from_all_exchanges(self):
        with self.mock_requests_odd():
            self.assertEqual(get_monero_price_from_all_exchanges(), [Decimal('0.20'), Decimal('200.00'), Decimal('200.00'), 
                Decimal('200.00'), Decimal('200.00'), Decimal('200.00'), Decimal('250.00'), Decimal('398.17'), Decimal('398.17')])

    def test_get_monero_price_from_all_exchanges_not_threaded(self):
        with self.mock_requests_odd():
            self.assertEqual(get_monero_price_from_all_exchanges_not_threaded(), [Decimal('0.20'), Decimal('200.00'), Decimal('200.00'), 
                Decimal('200.00'), Decimal('200.00'), Decimal('200.00'), Decimal('250.00'), Decimal('398.17'), Decimal('398.17')])

    def test_average_price(self):
        with self.mock_requests_odd():
            self.assertEqual(average_price(), Decimal('227.39'))

    def test_average_price_failure(self):
        with mock.patch('monero_usd_price.monero_usd_price.price_request', return_value=False):
            self.assertEqual(average_price(), None)

    def test_average_price_not_threaded(self):
        with self.mock_requests_odd():
            self.assertEqual(average_price_not_threaded(), Decimal('227.39'))

    def test_average_price_not_threaded_failure(self):
        with mock.patch('monero_usd_price.monero_usd_price.price_request', return_value=False):
            self.assertEqual(average_price_not_threaded(), None)

    def test_median_price_not_threaded(self):
        with self.mock_requests_odd():
            self.assertEqual(median_price_not_threaded(), Decimal('200.00'))
        with self.mock_requests_even():
            self.assertEqual(median_price_not_threaded(), Decimal('200.00'))
 
    def test_median_price_not_threaded_failure(self):
        with mock.patch('monero_usd_price.monero_usd_price.price_request', return_value=False):
            self.assertEqual(median_price_not_threaded(), None)

    def test_calculate_monero_from_usd(self):
        with self.mock_requests_odd():
            self.assertEqual(calculate_monero_from_usd(Decimal('100')), Decimal('0.5'))

    def test_calculate_usd_from_monero(self):
        with self.mock_requests_odd():
            self.assertEqual(calculate_usd_from_monero(Decimal('1.5')), Decimal('300'))

    def test_calculate_atomic_units_from_monero(self):
        self.assertEqual(calculate_atomic_units_from_monero(Decimal('1.2342')), 1234200000000)

    def test_calculate_monero_from_atomic_units(self):
        self.assertEqual(calculate_monero_from_atomic_units(1024150), Decimal('.00000102415'))

    def test_failing_response(self):
        with requests_mock.Mocker() as m:
            self.failed_coingecko_request(m)
            self.assertEqual(coingecko(), False)

    def test_exception(self):
        with mock.patch('requests.get', side_effect=Exception('Mocked exception')):
            self.assertEqual(coingecko(), False)

    def test_coingecko(self):
        with requests_mock.Mocker() as m:
            self.coingecko_request(m)
            self.assertEqual(coingecko(), Decimal('398.17'))
    
    # def test_coinmarketcap(self):
    #     with requests_mock.Mocker() as m:
    #         m.get('https://coinmarketcap.com/currencies/monero/', content=[{'price_usd': '398.17'}])
    #         self.assertEqual(coinmarketcap(), Decimal('398.17'))
    
    def test_cryptocompare(self):
        with requests_mock.Mocker() as m:
            self.cryptocompare_request(m)
            self.assertEqual(cryptocompare(), Decimal('398.17'))
    
    def test_kraken(self):
        with requests_mock.Mocker() as m:
            self.kraken_request(m)
            self.assertEqual(kraken(), Decimal('200.00'))
    
    def test_bitfinex(self):
        with requests_mock.Mocker() as m:
            self.bitfinex_request(m)
            self.assertEqual(bitfinex(), Decimal('200.00'))
    
    def test_poloniex(self):
        with requests_mock.Mocker() as m:
            self.poloniex_request(m)
            self.assertEqual(poloniex(), Decimal('0.20'))
    
    def test_huobi(self):
        with requests_mock.Mocker() as m:
            self.huobi_request(m)
            self.assertEqual(huobi(), Decimal('200.00'))
    
    def test_kucoin(self):
        with requests_mock.Mocker() as m:
            self.kucoin_request(m)
            self.assertEqual(kucoin(), Decimal('250.00'))
    
    def test_hitbtc(self):
        with requests_mock.Mocker() as m:
            self.hitbtc_request(m)
            self.assertEqual(hitbtc(), Decimal('200.00'))

    def test_binance(self):
        with requests_mock.Mocker() as m:
            self.binance_request(m)
            self.assertEqual(binance(), Decimal('200.00'))
