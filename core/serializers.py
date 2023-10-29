from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model

from rest_framework import serializers

    

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'phone_number')
        read_only_fields = ('id',)  
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'assigned_to', 'priority')
        read_only_fields = ('id',)
