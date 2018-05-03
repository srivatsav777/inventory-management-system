from rest_framework import serializers
from .models import processes
from .models import instances
from .models import task

class processesSerializer(serializers.ModelSerializer):
     
   class Meta:
     model=processes
     fields='__all__' 


class instancesSerializer(serializers.ModelSerializer):
     
   class Meta:
     model=instances
     fields='__all__' 

class taskSerializer(serializers.ModelSerializer):
     
   class Meta:
     model=task
     fields='__all__' 


