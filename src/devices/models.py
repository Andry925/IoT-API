import os
import peewee
import peewee_async
from src.location.models import Location
from src.users.models import User
from src.utilities import PasswordHasher

db = peewee_async.PostgresqlDatabase(
    "postgres",
    user='postgres',
    password="postgres",
    host='postgres',
    port=5432
)
class Device(peewee.Model, PasswordHasher):
    name = peewee.TextField()
    type = peewee.CharField(max_length=255)
    login = peewee.CharField(max_length=255, unique=True)
    password = peewee.CharField()
    location_id = peewee.ForeignKeyField(Location, related_name="location_devices")
    api_user_id = peewee.ForeignKeyField(User, related_name="user_devices")

    class Meta:
        database = db