from django.db import models
from rest_framework.generics import GenericAPIView
import uuid


class BaseModel(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ["id", "-updated_at"]


class BaseView(GenericAPIView):
    pass
