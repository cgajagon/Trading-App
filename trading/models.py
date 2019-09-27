from django.db import models
from django.urls import reverse, reverse_lazy
import datetime

class Symbols(models.Model):
    AD = 'ADR'
    RE = 'REIT'
    CE = 'Closed end fund'
    SI = 'Secondary Issue'
    LP = 'Limited Partnerships'
    CS = 'Common Stock'
    ET = 'ETF'
    TYPE = [
        (AD, 'ADR'),
        (RE, 'REIT'),
        (CE, 'Closed end fund'),
        (SI, 'Secondary Issue'),
        (LP, 'Limited Partnerships'),
        (CS, 'Common Stock'),
        (ET, 'ETF'),
    ]

    symbol = models.CharField(max_length=20, null=False, blank=False, unique=True, primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    isEnabled = models.BooleanField(null=False, blank=False, default=True)
    iexId = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
    symbol_type = models.CharField(max_length=20, choices=TYPE, default='AD')
    
    def __str__(self):
        return self.symbol


class SymbolsAutocomplete(models.Model):
    search = models.CharField(max_length=20, null=False, blank=False, unique=True, primary_key=True)

    def __str__(self):
        return self.search

class SymbolsAutocompleteRelation(models.Model):
    symbol = models.CharField(max_length=20, null=False, blank=False)
    search = models.ForeignKey(SymbolsAutocomplete, on_delete=models.CASCADE, null=False, blank=False, related_name='related_symbols')

class WatchSymbols(models.Model):
    symbol = models.OneToOneField(Symbols, on_delete=models.CASCADE, null=False, blank=False)
    date_enter = models.DateField(default=datetime.date.today)
    notes = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '%s on %s' % (self.symbol, self.date_enter)

class AlertWatch(models.Model):
    watched_symbol = models.ForeignKey(WatchSymbols, on_delete=models.CASCADE, null=False, blank=False)
    date_enter = models.DateField(default=datetime.date.today)
    expected_min_price = models.FloatField(null=False, blank=False)
    expected_max_price = models.FloatField(null=False, blank=False)
    notes = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return '%s on %s' % (self.watched_symbol, self.date_enter)

    # Return to Watch Symbol Detail View
    def get_absolute_url(self):
        return reverse_lazy('watchsymbol_detail', args=[str(self.watched_symbol.pk)])

class HistoricalPrices(models.Model):
    symbol = models.ForeignKey(Symbols, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(default=datetime.date.today)
    open_price = models.FloatField(null=True, blank=True)
    high_price = models.FloatField(null=True, blank=True)
    low_price = models.FloatField(null=True, blank=True)
    close_price = models.FloatField(null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)
    uOpen = models.FloatField(null=True, blank=True)
    uHigh = models.FloatField(null=True, blank=True)
    uLow = models.FloatField(null=True, blank=True)
    uClose = models.FloatField(null=True, blank=True)
    uVolume = models.IntegerField(null=True, blank=True)
    change = models.FloatField(null=True, blank=True)
    changePercent = models.FloatField(null=True, blank=True)
    changeOverTime = models.FloatField(null=True, blank=True)