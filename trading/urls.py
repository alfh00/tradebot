from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TradingBotViewSet, activate_trading_bot

router = DefaultRouter()
router.register(r'bots', TradingBotViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('activate/<int:bot_id>/', activate_trading_bot, name='activate_trading_bot'),
]
