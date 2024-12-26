from django.db import models

class FlowerPrediction(models.Model):
    image = models.ImageField(upload_to='flowers/')
    prediction = models.CharField(max_length=100)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)