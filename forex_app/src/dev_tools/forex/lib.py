import requests

from .utils import validate


class HandleRequest(object):
    """
    Class handles request and responses for 1forge.com.
        - api_key: is required parameter, you will get it from 1forge.com after registration process.

    Usage:
        >>> handle_request = HandleRequest(token='YOUR_TOKEN_XYZ')
        >>> handle_request.request(HandleRequest.ENDPOINT_QUOTES, **{"pairs": "EURUSD,GBPJPY,AUDUSD"})
        >>> handle_request.request(HandleRequest.ENDPOINT_SYMBOLS)
        >>> handle_request.request(HandleRequest.ENDPOINT_CONVERT, **{"from": "USD", "to": "EUR", "quantity": 1000})
        >>> handle_request.request(HandleRequest.ENDPOINT_MARKET_STATUS)
        >>> handle_request.request(HandleRequest.ENDPOINT_QUOTA)
    """
    DOMAIN = 'forex.1forge.com'
    API_VERSION = "1.0.3"
    PROTOCOL = "https"

    ENDPOINT_QUOTES = "quotes"
    ENDPOINT_SYMBOLS = "symbols"
    ENDPOINT_CONVERT = "convert"
    ENDPOINT_MARKET_STATUS = "market_status"
    ENDPOINT_QUOTA = "quota"

    endpoints = {
        ENDPOINT_QUOTES: "quotes?pairs={pairs}&",
        ENDPOINT_SYMBOLS: "symbols?",
        ENDPOINT_CONVERT: "convert?from={from}&to={to}&quantity={quantity}&",
        ENDPOINT_MARKET_STATUS: "market_status?",
        ENDPOINT_QUOTA: "quota?"
    }

    def __init__(self, api_key):
        self.api_key = api_key

    @validate
    def request(self, endpoint, **params):
        """
        Method returns json object.
        """
        prepared_endpoint = self.endpoints[endpoint].format(**params)
        url = "{protocol}://{domain}/{api_version}/{endpoint}api_key={api_key}".format(
            protocol=self.PROTOCOL,
            domain=self.DOMAIN,
            api_version=self.API_VERSION,
            endpoint=prepared_endpoint,
            api_key=self.api_key
        )

        response = requests.get(url)
        return response.json()


class Forex(object):
    def __init__(self, api_key):
        self.handle_request = HandleRequest(api_key)

    def list_quotes(self, pairs):
        """List quotes for specific currency pair(s)."""
        return self.handle_request.request(HandleRequest.ENDPOINT_QUOTES, **{"pairs": pairs})

    def list_symbols(self):
        """Get list of symbols."""
        return self.handle_request.request(HandleRequest.ENDPOINT_SYMBOLS)

    def convert_currencies(self, from_currency, to_currency, quantity):
        """Convert from one currency to another."""
        return self.handle_request.request(HandleRequest.ENDPOINT_CONVERT,
                                           **{"from": from_currency, "to": to_currency, "quantity": quantity})

    def get_market_status(self):
        """Check if the market is open."""
        return self.handle_request.request(HandleRequest.ENDPOINT_MARKET_STATUS)

    def get_quota(self):
        """Check current usage and remaining quota."""
        return self.handle_request.request(HandleRequest.ENDPOINT_QUOTA)

    def get_default_quotes(self, basic_currency):
        """Return default quotes."""
        default = ['EUR', 'USD', 'GBP', 'JPY']

        if basic_currency in default:
            default.remove(basic_currency)

        pairs = ""

        for currency in default:
            pairs += "{basic_currency}{currency},".format(basic_currency=basic_currency, currency=currency)

        return self.handle_request.request(HandleRequest.ENDPOINT_QUOTES, **{"pairs": pairs[:-1]})

