#from riskapi.models import risktype,risk
#from riskapi.serializers import RiskTypeSerializer,RiskSerializer
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from django_filters import rest_framework as filters

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'email', 'is_staff',)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'email', 'is_staff',)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class RiskTypeKeyList(generics.ListAPIView):
    queryset = risktype.objects.all()
    serializer_class = RiskTypeKeySerializer
    permission_classes = (permissions.IsAuthenticated,)    
    # http_method_names = ['get']

class RiskKeyList(generics.ListAPIView):
    queryset = risk.objects.all()
    serializer_class = RiskKeySerializer
    permission_classes = (permissions.IsAuthenticated,)    
    # http_method_names = ['get']

class RiskTypeList(generics.ListCreateAPIView):
    queryset = risktype.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'risk_type_name',)
    serializer_class = RiskTypeSerializer
    permission_classes = (permissions.IsAdminUser,)
    # http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.save(createdby=self.request.User)

class RiskTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = risktype.objects.all()
    # risktype = risktype.objects.get(pk=pk)
    serializer_class = RiskTypeSerializer
    permission_classes = (permissions.IsAdminUser,)

class RiskList(generics.ListCreateAPIView):
    queryset = risk.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'risk_name',)
    serializer_class = RiskSerializer    
    permission_classes = (permissions.IsAuthenticated,)
    # http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.save(createdby=self.request.User)

class RiskDetail(generics.RetrieveUpdateDestroyAPIView):
    # risk = risk.objects.get(pk=pk)
    queryset = risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = (permissions.IsAuthenticated,)
