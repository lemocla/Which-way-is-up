'''
Models for newsletter mailing list
'''
from django.db import models


# Create your models here.
class Mailing(models.Model):
    '''
    Model to register email address
    '''
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)

    class Meta:
        # Add verbose name
        verbose_name = 'Mailing List'
    
    def __str__(self):
        return str(self.email)
