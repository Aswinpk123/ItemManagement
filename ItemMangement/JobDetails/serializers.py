
from .models import *
from Item.models import *
from Driver.models import *
from Item.serializers import *
from Driver.serializers import *
from rest_framework import serializers



class JobSerializer(serializers.ModelSerializer):
  
    assigneddriver = serializers.SerializerMethodField()
    itemname = serializers.SerializerMethodField()
    itemtype = serializers.SerializerMethodField()
    # jobrefered = serializers.SerializerMethodField()

    class Meta:
        model = JobModels
        fields = '__all__'



    def get_assigneddriver(self,obj):
       

        v_obj = DetailsModel.objects.filter(id=obj.assigneddriver.id)
        v_qs = DetailsSerializerwithoutdoc(v_obj, many=True)
        
        return v_qs.data


    def get_itemname(self,obj):
       

        v_obj = ItemModel.objects.filter(id=obj.itemname.id)
        v_qs = ItemSerializerforjob(v_obj, many=True)
        
        return v_qs.data

    def get_itemtype(self,obj):
       

        v_obj = ItemTypeModel.objects.filter(id=obj.itemtype.id)
        v_qs = ItemTypeSerializer(v_obj, many=True)
        
        return v_qs.data

    # def get_jobrefered(self,obj):
       
    #     if obj.jobrefered == None:
    #         v_obj = DetailsModel.objects.all()
    #         v_qs = DetailsSerializerwithoutdoc(v_obj, many=True)
        
    #         return v_qs.data
    #     else:
    #         v_obj = DetailsModel.objects.filter(id=obj.jobrefered.id)
    #         v_qs = DetailsSerializerwithoutdoc(v_obj, many=True)
        
    #         return v_qs.data


        
        
        