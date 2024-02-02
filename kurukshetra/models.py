from django.db import models

class Input(models.Model):
    destination = models.TextField()

class Recommendations(models.Model):
    recommendations = models.TextField()