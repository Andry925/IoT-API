from users.models import db, User
from location.models import Location
from devices.models import Device

def create_tables():
    with db:
        db.create_tables([User, Location, Device])

create_tables()