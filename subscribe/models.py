'''
Models for newsletter subscription
'''
from django.db import models


# Create your models here.
class Subscription(models.Model):
    '''
    Model to register email address
    '''
    email = models.EmailField(max_length=255, null=False, blank=False)

    def __str__(self):
        return str(self.email)
