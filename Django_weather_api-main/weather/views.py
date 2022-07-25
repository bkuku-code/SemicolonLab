import re
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
import requests
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(('GET',))
@permission_classes([IsAuthenticated])
def authenticatewetheruser(request):
    key = '7f9c3189efea461d949161711221907'
    data = request.user
    location = data.location
    try:
        weather_request = requests.get("https://api.weatherapi.com/v1/current.json?key=" + key + "&q=" + location)
        data = json.loads(weather_request.content)
        return Response(data)
    except ObjectDoesNotExist:
        pass


@api_view(('POST',))
@csrf_exempt
def unauthenticateduser(request):
    key = '7f9c3189efea461d949161711221907'
    location = request.data['location']
    try:
        URL = 'https://api.weatherapi.com/v1/current.json'
        PARAMS = {'key': key, 'q': location}
        weather_request = requests.get(url=URL, params=PARAMS)
        # weather_request = requests.get("https://api.weatherapi.com/v1/current.json?key="+key+"&q="+location)
        data = json.loads(weather_request.content)
        return Response(data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        pass


@api_view(('GET', 'POST'))
@permission_classes([IsAuthenticated])
def authenticateduser_with_days(request):
    key = '7f9c3189efea461d949161711221907'
    data = request.user
    location = data.location
    days = request.data['days']
    number_of_days_allowed = 10
    if days <= number_of_days_allowed:
        converted_days = str(days)
        weather_request = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?key=" + key + "&q=" + location + "&days=" + converted_days)
        data = json.loads(weather_request.content)
        return Response(data)
    else:
        notfound = 'Kindly Enter a value less than or equal to 10'
        return Response(notfound, status=status.HTTP_404_NOT_FOUND)


@api_view(('POST',))
@csrf_exempt
def unauthenticateduser_with_days(request):
    key = '7f9c3189efea461d949161711221907'
    location = request.data['location']
    days = request.data['days']
    number_of_days_allowed = 14
    try:
        if days <= number_of_days_allowed:
            URL = 'https://api.weatherapi.com/v1/forecast.json'
            PARAMS = {'key': key, 'q': location, 'days': days}
            weather_request = requests.get(url=URL, params=PARAMS)
            data = json.loads(weather_request.content)
            return Response(data, status=status.HTTP_200_OK)
        else:
            notfound = 'Kindly Enter a value less than or equal to 10'
            return Response(notfound, status=status.HTTP_404_NOT_FOUND)

    except ObjectDoesNotExist:
        pass
