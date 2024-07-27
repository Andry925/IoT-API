import peewee
import peewee_async
from decouple import config
from src.utilities import PasswordHasher

db = peewee_async.PostgresqlDatabase(
    config('name'),
    user=config('user'),
    password=config('password'),
    host=config('host'),
    port=config('port')
)



class User(peewee.Model, PasswordHasher):
    name = peewee.CharField(max_length=128)
    email = peewee.CharField(unique=True)
    password = peewee.CharField()

    class Meta:
        database = db
        table_name = "api_user"
