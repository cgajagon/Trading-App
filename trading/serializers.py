from rest_framework import serializers
from trading import models


class SymbolsSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='symbol_type')
    class Meta:
        model = models.Symbols
        fields = '__all__'   
    
    def create(self, validated_data):
        symbol, created = Symbols.objects.update_or_create(
        symbol=validated_data.get('symbol', None),
        defaults={'symbol': validated_data.get('symbol', None)}
        )
        return symbol