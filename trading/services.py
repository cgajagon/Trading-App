import requests
import json
import pandas as pd
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status

from trading import serializers, models

# 3rd Part API: iextrading.com
def get_symbols():
    url = 'https://api.iextrading.com/1.0/ref-data/symbols'
    response = requests.get(url)
    if response.status_code==200:
        symbols = response.json()
        return symbols
    else:
        print("There is no connexion")

def get_quote(symbol):
    endpoint = 'https://api.iextrading.com/1.0/tops/last?symbols={symbol}'
    url = endpoint.format(symbol=symbol)
    response =requests.get(url)
    if response.status_code==200:
        quote = response.json()
        return quote
    else:
        print("There is no connexion")

def get_chart_data(symbol, time_interval):
    endpoint = 'https://sandbox.iexapis.com/stable/stock/{symbol}/chart/{time_interval}?token=Tpk_e023b4e95edb425c9dc89ee4c6972086'
    url = endpoint.format(symbol=symbol, time_interval=time_interval)
    response =requests.get(url)
    if response.status_code==200:
        history = response.json()
        # Trasnform output
        df = pd.DataFrame(history)
        df_resample = pd.DataFrame(columns=['min_close','min_open','max_high','min_low', 'mean_volume'])
        interval = 'M'
        df['date'] = pd.to_datetime(df['date'])
        df.index = df['date'] 
        df_resample['min_close'] = df['close'].resample(interval).min()
        df_resample['min_open'] = df['open'].resample(interval).min()
        df_resample['max_high'] = df['high'].resample(interval).max()
        df_resample['min_low'] = df['low'].resample(interval).min()
        df_resample['mean_volume'] = df['volume'].resample(interval).mean()
        df_resample['date'] = df_resample.index.date
        data = df_resample.to_dict('records')
        #data = {
        #        'date':list(df_resample['date']),
        #        'high':list(df_resample['max_high']),
        #        'low':list(df_resample['min_low']),
        #        'open':list(df_resample['min_open']),
        #        'close':list(df_resample['min_close']),
        #        'volume':list(df_resample['mean_volume']),
        #}
        return data
    else:
        print("There is no connexion")

def get_history_data(symbol, time_interval):
    endpoint = 'https://sandbox.iexapis.com/stable/stock/{symbol}/chart/{time_interval}?token=Tpk_e023b4e95edb425c9dc89ee4c6972086'
    url = endpoint.format(symbol=symbol, time_interval=time_interval)
    response =requests.get(url)
    if response.status_code==200:
        history = response.json()
        return history
    else:
        print("There is no connexion")


# 3rd Part API: yahoo-finance.com
def get_chart_data2(symbol, time_interval, time_range):
    endpoint = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart?interval={interval}&region=US&symbol={symbol}&lang=en&range={range}"
    url = endpoint.format(source_lang='en', region='US', symbol=symbol, interval=time_interval, range=time_range )
    headers = {'X-RapidAPI-Host': settings.X_RapidAPI_Host, 'X-RapidAPI-Key': settings.X_RapidAPI_Key}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data