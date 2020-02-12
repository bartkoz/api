from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

from insurance.factories import CustomerFactory
from insurance.models import Customer, PolicyRequest


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_customer_proper_payload(self):
        count = Customer.objects.count()
        r = self.client.post(reverse('insurance:api_create_customer'),
                             {"first_name": "John",
                              "last_name": "Doe",
                              "dob": "01-01-1900"})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(Customer.objects.count(), count + 1)

    def test_create_customer_improper_payload(self):
        count = Customer.objects.count()
        r = self.client.post(reverse('insurance:api_create_customer'),
                             {"last_name": "Doe",
                              "dob": "01-01-1900"})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(Customer.objects.count(), count)

    def test_create_policy_request_proper_payload(self):
        customer = CustomerFactory.create()
        customer.save()
        count = PolicyRequest.objects.count()
        r = self.client.post(reverse('insurance:api_create_policy'),
                             {"type": "personal-accident",
                              "premium": 100,
                              "cover": 123,
                              "customer": customer.pk})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(PolicyRequest.objects.count(), count+1)

    def test_create_policy_request_improper_payload(self):
        customer = CustomerFactory.create()
        customer.save()
        count = PolicyRequest.objects.count()
        r = self.client.post(reverse('insurance:api_create_policy'),
                             {"type": "personal-accident",
                              "premium": 100,
                              "cover": 123})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(PolicyRequest.objects.count(), count)
