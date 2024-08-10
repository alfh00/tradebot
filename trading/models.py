from django.db import models
from django.contrib.auth.models import User
from strategies.models import Strategy

class TradingBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s {self.strategy.name} Bot"
