import requests
import json
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status

from trading.serializers import SymbolsSerializer

def get_books(symbol):
    url = 'http://api.example.com/books'
    endpoint = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/{symbol}/time-series"
    url = endpoint.format(source_lang='en', symbol=symbol, region='US')
    headers = {'X-RapidAPI-Host': settings.OXFORD_APP_ID, 'X-RapidAPI-Key': settings.OXFORD_APP_KEY}
    response = requests.get(url, headers=headers)
    books = response.json()
    books_list = {'books':books['results']}
    return books_list

def get_symbols():
    url = 'https://api.iextrading.com/1.0/ref-data/symbols'
    response = requests.get(url)
    symbols = response.json()
    return symbols

def get_quote(symbol):
    endpoint = 'https://api.iextrading.com/1.0/deep?symbols={symbol}'
    url = endpoint.format(symbol=symbol)
    response = requests.get(url)
    quote = response.json()
    return quote

def get_history(symbol):
    endpoint = 'https://sandbox.iexapis.com/stable/stock/{symbol}/chart/max?token=Tpk_e023b4e95edb425c9dc89ee4c6972086'
    url = endpoint.format(symbol=symbol)
    response =requests.get(url)
    history = response.json()
    return history

