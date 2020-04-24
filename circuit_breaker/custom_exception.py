from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

from circuit_breaker.quickstart.views import breaker


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print(response)
    response.data['detail'] = 'error...'
    return response
