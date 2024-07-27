import peewee
import peewee_async
from decouple import config

db = peewee_async.PostgresqlDatabase(
    config('name'),
    user=config('user'),
    password=config('password'),
    host=config('host'),
    port=config('port')
)


class Location(peewee.Model):
    name = peewee.CharField(unique=True)

    class Meta:
        database = db
