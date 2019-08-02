from django.db import models
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

class WatchSymbols(models.Model):
    symbol = models.ForeignKey(Symbols, on_delete=models.CASCADE, null=False, blank=False)
    date_enter = models.DateField(default=datetime.date.today)
    notes = models.TextField(max_length=200)
