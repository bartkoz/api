from datetime import datetime

import factory
from factory.fuzzy import FuzzyInteger

from .models import Customer, PolicyRequest


class CustomerFactory(factory.Factory):

    class Meta:
        model = Customer

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    dob = datetime.now()


class PolicyRequestFactory(factory.Factory):

    class Meta:
        model = PolicyRequest

    customer = CustomerFactory.create().save()
    premium = FuzzyInteger(1, 100)
    cover = FuzzyInteger(1, 100)
    type = 'personal-accident'
