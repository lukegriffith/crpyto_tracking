'''
Module is used to query gdax api and convert results into GBP.
'''

import gdax
from forex_python.converter import CurrencyRates


class Crypto_stats:
    '''
    Crypto_Stats performs actions to query API and convert currency.
    '''

    def __init__(self):

        self.pub_client = gdax.PublicClient()
        self.currency_rates = CurrencyRates()


    def get_ether_gbp(self):
        '''
        Returns ethereum price in GBP
        '''

        usd = self.pub_client.get_product_ticker(product_id="ETH-USD")
        decimal_price = float(usd["price"])
        gbp_price = self.currency_rates.convert('USD', 'GBP', decimal_price)


        return gbp_price
