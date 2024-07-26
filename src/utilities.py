from users.models import db, User

def create_tables():
    with db:
        db.create_tables([User])

create_tables()