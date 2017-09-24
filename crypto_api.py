'''
Flask app for crypto api.
Currently exposes price of ethereum, in GBP from GDAX api.
'''
from flask import Flask
from cryptostats import Crypto_stats

app = Flask(__name__)

ether_stats = Crypto_stats()

@app.route("/")
def ether():
    return str(ether_stats.get_ether_gbp())
    