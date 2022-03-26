from rest_framework import serializers
from .models import *


class ChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargesModel
        fields = '__all__'