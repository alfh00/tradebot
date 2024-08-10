from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TradingBot
from .serializers import TradingBotSerializer
from .tasks import execute_trading_bot

class TradingBotViewSet(viewsets.ModelViewSet):
    queryset = TradingBot.objects.all()
    serializer_class = TradingBotSerializer


@api_view(['POST'])
def activate_trading_bot(request, bot_id):
    bot = TradingBot.objects.get(id=bot_id)
    bot.is_active = True
    bot.save()
    #execute_trading_bot.delay(bot_id)
    return Response({'message': 'Trading bot activated'}, status=200)