from rest_framework import serializers
from .models import UserAPIKey

class UserAPIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAPIKey
        fields = ['api_key', 'api_secret']
