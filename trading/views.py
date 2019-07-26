from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import JsonResponse, HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


import json
import requests
import pandas as pd

from trading.forms import DictionaryForm, QuoteForm, SymbolForm
from trading import models
from trading import serializers
from trading import services


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ModelViewSet


class HomePageView(TemplateView):
    template_name = "trading/index.html"

class SymbolsListView(ListView):
    template_name = "trading/symbols.html"
    model = models.Symbols
    context_object_name = 'symbols_list'

class SymbolsListView2(TemplateView):
    template_name = 'trading/symbols.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['symbols_list'] = services.get_symbols()
        return context

class WatchSymbolListView(ListView):
    model = models.WatchSymbols
    context_object_name = 'project_list'
    template_name = 'trading/watchsymbols_list.html'

class WatchSymbolCreateView(CreateView):
    model = models.WatchSymbols
    fields = '__all__'
    template_name = 'trading/watchsymbols_new.html'
    success_url = reverse_lazy('trading:project_list')

class WatchSymbolDeleteView(DeleteView):
    model = models.WatchSymbols
    success_url = reverse_lazy('trading:tool_list')

class WatchSymbolDetailView(DetailView):
    model = models.WatchSymbols
    template_name = 'trading/watchsymbols_detail.html'

class WatchSymbolUpdateView(UpdateView):
    model = models.WatchSymbols
    template_name = 'trading/watchsymbols_update.html'
    fields = '__all__'

def HistoryList(request):
    symbols_list = services.get_symbols()
    search_result = {}
    if 'symbol' in request.GET:
        form = SymbolForm(request.GET)
        if form.is_valid():
            symbol = form.search()
            search_result = services.get_history(symbol)
    else:
        form = SymbolForm()
    return render(request, 'trading/historical.html', {'symbols_list': symbols_list, 'form': form, 'search_result': search_result})

class ChartHistoricalAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, symbol, format=None):
        raw_data = services.get_history(symbol)
        df = pd.DataFrame(raw_data)
        data = {
            'date':list(df['date']),
            'high':list(df['high']),
            'low':list(df['low']),
        }
        return Response(data)

