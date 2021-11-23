from uuid import uuid4

from django.db import models

from core.models import TimeStamp


class User(TimeStamp):
    id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name     = models.CharField(max_length = 32)
    email    = models.CharField(max_length = 64, unique = True)
    password = models.CharField(max_length = 128)

    class Meta:
        db_table = "users"
