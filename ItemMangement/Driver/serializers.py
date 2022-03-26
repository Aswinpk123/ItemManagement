from .models import *
from rest_framework import serializers

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = DocumentsModel
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True)
    class Meta:
        model  = DetailsModel
        fields = '__all__'


class DetailsSerializerwithoutdoc(serializers.ModelSerializer):
    class Meta:
        model  = DetailsModel
        fields = ('id','name','Phone','vehicle_number')