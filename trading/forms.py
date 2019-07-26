from django import forms
from django.conf import settings
import requests

from trading.services import get_quote, get_symbols, get_history

class DictionaryForm(forms.Form):
    symbol = forms.CharField(max_length=100)

    def search(self):
        result = {}
        symbol = self.cleaned_data['symbol']
        endpoint = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/{symbol}/time-series"
        url = endpoint.format(source_lang='en', symbol=symbol, region='US')
        headers = {'X-RapidAPI-Host': settings.OXFORD_APP_ID, 'X-RapidAPI-Key': settings.OXFORD_APP_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
        else:
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % symbol
            else:
                result['message'] = 'The API is not available at the moment. Please try again later.'
        return result

class QuoteForm(forms.Form):
    symbol = forms.CharField(max_length=100)

    def search(self):
        symbol = self.cleaned_data['symbol']
        quote = get_quote(symbol)
        return quote

class SymbolForm(forms.Form):
    symbol = forms.CharField(max_length=100)
    def search(self):
        symbol = 'AAPL'
        return symbol