from enum import Enum

from django.utils.translation import gettext_lazy as _


class Type(Enum):
    available = ('personal-accident', _('Personal accident'))

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]
