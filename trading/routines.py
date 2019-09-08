from trading import models, serializers, services
import pandas as pd
import requests
import json

def create_update_symbols():
    symbols = services.get_symbols
    for element in symbols:
        symbol_obj, created = models.Symbols.objects.update_or_create(
            symbol=element.get('symbol', None),
            defaults={
                'symbol': element.get('symbol', None),
                'name': element.get('name', None),
                'isEnabled': element.get('isEnabled', None),
                'iexId': element.get('iexId', None),
                'date': element.get('date', None),
                'symbol_type': element.get('type', None),
            }
        )

def create_update_history(symbol, range_time):
    history = services.get_history_data(symbol,range_time)
    for element in history:
        history_obj, created = models.HistoricalPrices.objects.filter(symbol=symbol).update_or_create(
            date=element.get('date', None),
            defaults={
                'symbol_id': symbol,
                'date': element.get('date', None),
                'open_price': element.get('open', None),
                'high_price': element.get('high', None),
                'low_price': element.get('low', None),
                'close_price': element.get('close', None),
                'volume': element.get('volume', None),
                'uOpen': element.get('uOpen', None),
                'uHigh': element.get('uHigh', None),
                'uLow': element.get('uLow', None),
                'uClose': element.get('uClose', None),
                'uVolume': element.get('uVolume', None),
                'change': element.get('change', None),
                'changePercent': element.get('changePercent', None),
                'changeOverTime': element.get('changeOverTime', None),
            }
        )

def get_recommendations():
    df_recomendation = pd.DataFrame()
    history = list(models.HistoricalPrices.objects.all().values())
    df_history = pd.DataFrame(history)
    for symbol in df_history.symbol_id.unique():
        df_slice = df_history.loc[df_history['symbol_id'] == symbol]
        max_high = df_slice.loc[df_slice["high_price"].idxmax()]
        df_recomendation = pd.DataFrame([max_high]).append(df_recomendation)
    print(df_recomendation)

def create_update_symbolsautocomplete():
    # Delete all the data in the SymbolsAutocomplete table and SymbolsAutocompleteRelated
    current_autocomplete = models.SymbolsAutocomplete.objects.all()
    current_autocomplete.delete()

    data = models.Symbols.objects.all().values("symbol")
    autocompleteList = list()
    searchList = list()

    for value in data:
        length = len(value['symbol'])
        cut = 1
        searchList.append(value['symbol'])
        new = models.SymbolsAutocomplete.objects.create(search=value['symbol'])
        new.symbolsautocompleterelation_set.create(symbol=value['symbol'])

        while cut < length:
            st = value['symbol']
            st = st[:-cut]
            cut += 1
            if st not in searchList:
                searchList.append(st)
                new = models.SymbolsAutocomplete.objects.create(search=st)
                new.symbolsautocompleterelation_set.create(symbol=value['symbol'])
            else:
                new = models.SymbolsAutocomplete.objects.get(search=st)
                new.symbolsautocompleterelation_set.create(symbol=value['symbol'])
        