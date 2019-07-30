from rest_framework import serializers
from trading import models

class SymbolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Symbols
        fields = '__all__'   