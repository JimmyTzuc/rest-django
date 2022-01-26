import uuid
from django.db import models

"""
Model solid method from all models
"""
class Resource(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        abstract = True



