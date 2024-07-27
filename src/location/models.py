import peewee
import peewee_async

db = peewee_async.PostgresqlDatabase(
    "postgres",
    user='postgres',
    password="postgres",
    host='postgres',
    port=5432
)


class Location(peewee.Model):
    name = peewee.CharField(unique=True)

    class Meta:
        database = db
