from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = False)

    class Meta:
        abstract = True
