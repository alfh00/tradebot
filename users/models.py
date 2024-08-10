from django.db import models

from django.db import models
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField


class UserAPIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = EncryptedCharField(max_length=50)
    api_secret = EncryptedCharField(max_length=50)

