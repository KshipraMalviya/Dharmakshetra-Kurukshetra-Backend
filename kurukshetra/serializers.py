from rest_framework import serializers
from .models import Input, Recommendations

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ['destination']

class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = ['recommendations']
