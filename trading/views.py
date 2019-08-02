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

from trading import forms
from trading import models
from trading import serializers
from trading import services


from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
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

class ChartView(TemplateView):
    template_name = 'trading/chart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        symbol = self.kwargs['symbol']
        context['symbol'] = models.Symbols.objects.get(symbol=symbol)
        context['range'] = self.kwargs['range']
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

# API Views
class SymbolsListAPI(ListAPIView):
    queryset = models.Symbols.objects.all()
    serializer_class = serializers.SymbolsSerializer

class ChartHistoricalAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, **kwargs):
        symbol = self.kwargs['symbol']
        range = self.kwargs['range']
        data = services.get_chart_data(symbol, range)  
    
        return Response(data)

class ChartHistoricalAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, **kwargs):
        symbol = self.kwargs['symbol']
        range = self.kwargs['range']
        data = services.get_chart_data(symbol, range)  
    
        return Response(data)

class ChartHistoricalAPI2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, symbol, time_interval, time_range, format=None):
        raw_data = services.get_chart_data2(symbol, time_interval, time_range)
        df = pd.DataFrame(raw_data)
        data = {
            'date':list(df['date']),
            'high':list(df['high']),
            'low':list(df['low']),
            'open':list(df['open']),
            'close':list(df['close']),
            'volume':list(df['volume']),
        }
        return Response(data)

