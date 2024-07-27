import peewee
import peewee_async
import os
from src.utilities import PasswordHasher

db = peewee_async.PostgresqlDatabase(
    "postgres",
    user='postgres',
    password="postgres",
    host='postgres',
    port=5432
)


class User(peewee.Model, PasswordHasher):
    name = peewee.CharField(max_length=128)
    email = peewee.CharField(unique=True)
    password = peewee.CharField()

    class Meta:
        database = db
        table_name = "api_user"
