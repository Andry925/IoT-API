import peewee
import peewee_async
from decouple import config

db = peewee_async.PostgresqlDatabase(database=config("DB_NAME"))


class Location(peewee.Model):
    name = peewee.CharField(unique=True)

    class Meta:
        database = db
