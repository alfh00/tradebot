
from celery import shared_task
from .models import TradingBot
from .trading_bot import TradingBotExecutor

@shared_task
def execute_trading_bot(bot_id):
    bot = TradingBot.objects.get(id=bot_id)
    executor = TradingBotExecutor(bot.api_key, bot.api_secret, bot.strategy.parameters)
    executor.run()
