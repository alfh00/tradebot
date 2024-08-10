from rest_framework import viewsets
from .models import Strategy
from .serializers import StrategySerializer

class StrategyViewSet(viewsets.ModelViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer
