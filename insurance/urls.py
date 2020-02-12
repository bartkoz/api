from django.urls import path

from . import views


app_name = 'insurance'
urlpatterns = [
    path('v1/create_customer/', views.CreateCustomerAPIView.as_view(), name='api_create_customer'),
    path('v1/create_policy/', views.CreatePolicyAPIView.as_view(), name='api_create_policy')
]
