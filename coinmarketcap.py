from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class CMC_Client:
    API_URL = "https://pro-api.coinmarketcap.com"

    #initial constractor
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
          'Accepts': 'application/json',
          'X-CMC_PRO_API_KEY': self.api_key,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    # for more detail about this function please visite this link : https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
    def listings_latest(self, **kwargs):
        url = self.API_URL+"/v1/cryptocurrency/listings/latest"
        parameters = {}
        for k in kwargs.keys():
            parameters[k] = kwargs[k]

        try:
            response = self.session.get(url, params = parameters)
            if response.status_code == 200:
                data = json.loads(response.text)
                json_string = json.dumps(data['data'])
                return json_string
            else :
                return response.text
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

    # for more detail about this function please visite this link : https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest
    def quotes_latest(self, **kwargs):
        url = self.API_URL+"/v2/cryptocurrency/quotes/latest"
        parameters = {}
        for k in kwargs.keys():
            parameters[k] = kwargs[k]

        try:
            response = self.session.get(url, params = parameters)
            if response.status_code == 200:
                data = json.loads(response.text)
                json_string = json.dumps(data['data'])
                return json_string
            else :
                return response.text
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

    # for more detail about this function please visite this link : https://coinmarketcap.com/api/documentation/v1/#operation/getV1KeyInfo
    def key_info(self):
        url = self.API_URL+"/v1/key/info"
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                json_string = json.dumps(data['data'])
                return json_string
            else :
                return response.text
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

    # for more detail about this function please visite this link : https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo
    def crypto_info(self, **kwargs):
        url = self.API_URL+"/v2/cryptocurrency/info"
        parameters = {}
        for k in kwargs.keys():
            parameters[k] = kwargs[k]

        try:
            response = self.session.get(url, params = parameters)
            if response.status_code == 200:
                data = json.loads(response.text)
                json_string = json.dumps(data['data'])
                return json_string
            else :
                return response.text
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

    # for more detail about this function please visite this link : https://coinmarketcap.com/api/documentation/v1/#operation/getV2ToolsPriceconversion
    def price_conversion(self, amount = 1, symbol = "BTC", **kwargs):
        url = self.API_URL+"/v2/tools/price-conversion"
        parameters = {"amount":amount, "symbol":symbol}
        for k in kwargs.keys():
            parameters[k] = kwargs[k]

        try:
            response = self.session.get(url, params = parameters)
            if response.status_code == 200:
                data = json.loads(response.text)
                json_string = json.dumps(data['data'])
                return json_string
            else :
                return response.text
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e

    # for more detail about this function please visite this link : https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest
    def global_metrics_quotes(self, **kwargs):
        url = self.API_URL+"/v1/global-metrics/quotes/latest"
        parameters = {}
        for k in kwargs.keys():
            parameters[k] = kwargs[k]

        try:
            response = self.session.get(url, params = parameters)
            if response.status_code == 200:
                data = json.loads(response.text)
                json_string = json.dumps(data['data'])
                return json_string
            else :
                return response.text
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            return e
