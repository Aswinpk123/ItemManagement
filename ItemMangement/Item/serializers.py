from dataclasses import field
from rest_framework import serializers
from .models import *


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTypeModel
        fields = '__all__'

# class ItemTypeSerializerforjob(serializers.ModelSerializer):
#     class Meta:
#         model = ItemTypeModel
#         fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'


class ItemSerializerforjob(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ('id','Itemname')