from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserAPIKey
from .serializers import UserAPIKeySerializer

class UserAPIKeyViewSet(viewsets.ModelViewSet):
    queryset = UserAPIKey.objects.all()
    serializer_class = UserAPIKeySerializer

@api_view(['POST'])
def store_api_key(request):
    user = request.user
    api_key = request.data.get('api_key')
    api_secret = request.data.get('api_secret')

    UserAPIKey.objects.update_or_create(user=user, defaults={'api_key': api_key, 'api_secret': api_secret})

    return Response({'message': 'API key stored successfully'}, status=200)
