from django.db import models

class Strategy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parameters = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

