import peewee
import peewee_async
import bcrypt
from decouple import config

db = peewee_async.PostgresqlDatabase(database=config("DB_NAME"))


class User(peewee.Model):
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    password = peewee.CharField()

    class Meta:
        database = db
        table_name = "api_user"

    def set_password(self, raw_password):
        raw_password_bytes = raw_password.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(raw_password_bytes, salt).decode('utf-8')

    def check_password(self, raw_password):
        raw_password_bytes = raw_password.encode('utf-8')
        return bcrypt.checkpw(
            raw_password_bytes,
            self.password.encode('utf-8'))
