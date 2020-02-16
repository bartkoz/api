from rest_framework import serializers

from insurance.models import Customer, PolicyRequest


class CustomerSerializer(serializers.ModelSerializer):

    dob = serializers.DateField(input_formats=["%d-%m-%Y", ])

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'dob')


class PolicyRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolicyRequest
        fields = ('type', 'premium', 'cover', 'customer')
