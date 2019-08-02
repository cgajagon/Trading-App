from trading import models, serializers
import requests
import pandas as pd

def create_update_symbols_table():
    url = 'https://api.iextrading.com/1.0/ref-data/symbols'
    response = requests.get(url)
    symbols = response.json()
    queryset = models.Symbols.objects.all().values()
    df_db = pd.DataFrame(list(queryset)).set_index("iexId")
    df_response = pd.DataFrame(symbols).set_index("iexId")
    df_db.update(df_response)
    df_db = pd.concat([df_db, df_response], sort=False).drop_duplicates()

def create_update_symbols():
    url = 'https://api.iextrading.com/1.0/ref-data/symbols'
    response = requests.get(url)
    symbols = response.json()
    #serializer = serializers.QuoteSerializer(data=symbols, many=True)
    #serializer.is_valid()
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

