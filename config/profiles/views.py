from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from .models import UserNet
from .serializers import GetUserNetSerializer,GetUsePublicNetSerializer
from rest_framework import permissions
from rest_framework import viewsets


class UserNetPublicView(viewsets.ModelViewSet):
    queryset = UserNet.objects.all()
    serializer_class = GetUsePublicNetSerializer
    permission_classes = [permissions.AllowAny]
    
class UserNetView(viewsets.ModelViewSet):
    
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self): 
        return UserNet.objects.filter(id=self.request.user.id)