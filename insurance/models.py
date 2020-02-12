from django.db import models
from django.utils.translation import gettext_lazy as _

from insurance.abstract import TimestampAbstractModel
from insurance.choices import Type


class Customer(TimestampAbstractModel):
    first_name = models.CharField(max_length=255,
                                  verbose_name=_('First name')
                                  )
    last_name = models.CharField(max_length=255,
                                 verbose_name=_('Last name')
                                 )
    dob = models.DateField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class PolicyRequest(TimestampAbstractModel):
    type = models.CharField(max_length=255,
                            choices=[x.value for x in Type],
                            verbose_name=_('Type')
                            )
    premium = models.PositiveIntegerField()
    cover = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('Customer')
                                 )

    def __str__(self):
        return '{} policy covering {}'.format(self.type, self.cover)
