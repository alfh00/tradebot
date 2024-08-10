from rest_framework import serializers
from .models import TradingBot

class TradingBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingBot
        fields = '__all__'
