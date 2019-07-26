from rest_framework import serializers
from trading import models

class SymbolsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='symbol_type')
    class Meta:
        model = models.Symbols
        fields = ('symbol','name', 'date', 'isEnabled', 'type', 'iexId')    