from functools import wraps

from .exceptions import RequestError


def validate(func):
    """
    Checks status code, raises exception if status_code isn't 200.
    """
    BAD_REQUEST = 400

    @wraps(func)
    def validate_response(instance, endpoint, **params):
        response = func(instance, endpoint, **params)
        if 'error' in response and response.get('error') is True:
            message = {
                'status_code': BAD_REQUEST,
                'description': response.get('message')
            }
            raise RequestError(message)

        return response

    return validate_response




