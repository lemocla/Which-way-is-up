"""
Case insenstive field
"""

from django.db.models import CharField

from django_case_insensitive_field import CaseInsensitiveFieldMixin


class CaseInsensitiveCharField(CaseInsensitiveFieldMixin, CharField):
    """
    Makes django CharField case insensitive
    Extends both the `CaseInsensitiveMixin` and  CharField
    Then you can import
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
