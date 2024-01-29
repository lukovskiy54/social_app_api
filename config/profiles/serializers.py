from rest_framework import serializers
from .models import UserNet
from django.contrib.auth.hashers import make_password

class GetUserNetSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserNet
        exclude = ("password","last_login","is_staff","is_superuser","is_active","email","groups","user_permissions")
        
   
    
class GetUsePublicNetSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserNet
        exclude = ("password","last_login","is_staff","is_superuser","is_active","email","groups","user_permissions")
        
    