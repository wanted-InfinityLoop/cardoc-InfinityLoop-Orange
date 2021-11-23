from uuid import uuid4

from django.db import models

from core.models import TimeStamp


class FrontTire(TimeStamp):
    id           = models.UUIDField(primary_key=True, default=uuid4().hex, editable=False)
    width        = models.PositiveSmallIntegerField()
    aspect_ratio = models.PositiveSmallIntegerField()
    wheel_size   = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'front_tires'


class RearTire(TimeStamp):
    id           = models.UUIDField(primary_key=True, default=uuid4().hex, editable=False)
    width        = models.PositiveSmallIntegerField()
    aspect_ratio = models.PositiveSmallIntegerField()
    wheel_size   = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'front_tires'


class Car(TimeStamp):
    id         = models.UUIDField(primary_key=True, default=uuid4().hex, editable=False)
    user       = models.ForeignKey('users.User', on_delete = models.CASCADE)
    model_name = models.CharField(max_length = 64)
    front_tire = models.ForeignKey('FrontTire', null = True, on_delete = models.SET_NULL)
    rear_tire  = models.ForeignKey('RearTire', null = True, on_delete = models.SET_NULL)

    class Meta:
        db_table = 'rear_tires'
