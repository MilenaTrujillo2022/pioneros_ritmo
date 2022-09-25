from rest_framework import serializers
from api.models import Eps

class EpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eps
        fields=['id','nombre']