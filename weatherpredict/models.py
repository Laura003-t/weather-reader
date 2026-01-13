from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WeatherSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    description = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['searched_at']

    def __str__(self):
        return f"{self.user.username} - {self.city} at {self.searched_at}"