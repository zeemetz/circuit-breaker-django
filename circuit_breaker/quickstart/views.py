import random

import pybreaker
from circuitbreaker import circuit
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from circuit_breaker.my_exception import MyException
from circuit_breaker.quickstart.serializer import UserSerializer, GroupSerializer

breaker = pybreaker.CircuitBreaker(fail_max=4, reset_timeout=10)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@breaker
def error_client():
    raise Exception
    pass


@api_view(['GET'])
def hello_world(request, greeting):
    print(greeting)
    print(request.data)
    while 1:
        print( "loops")

    if greeting == 'error':
        try:
            error_client()
        except Exception:
            raise APIException
    return Response(greeting)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
