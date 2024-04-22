from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Consumer,ConsumerLoan
from .models import Provider, Consumer, ProviderLoan, ConsumerLoan
from .serializers import ProviderSerializer, ConsumerSerializer, ProviderLoanSerializer, ConsumerLoanSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

class ProviderLoanViewSet(viewsets.ModelViewSet):
    queryset = ProviderLoan.objects.all()
    serializer_class = ProviderLoanSerializer

class ConsumerLoanViewSet(viewsets.ModelViewSet):
    queryset = ConsumerLoan.objects.all()
    serializer_class = ConsumerLoanSerializer