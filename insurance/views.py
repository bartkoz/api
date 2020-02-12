from rest_framework import generics

from insurance.models import Customer, PolicyRequest
from insurance.serializers import CustomerSerializer, PolicyRequestSerializer


class CreateCustomerAPIView(generics.CreateAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CreatePolicyAPIView(generics.CreateAPIView):

    serializer_class = PolicyRequestSerializer
    queryset = PolicyRequest.objects.all()
