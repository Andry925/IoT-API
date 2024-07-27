from src.users.models import db


def create_tables():
    create_location_table = """
    CREATE TABLE IF NOT EXISTS Location (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL UNIQUE
    );
    """

    create_user_table = """
    CREATE TABLE IF NOT EXISTS api_user (
        id SERIAL PRIMARY KEY,
        name VARCHAR(128) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );
    """

    create_device_table = """
    CREATE TABLE IF NOT EXISTS Device (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        type VARCHAR(255) NOT NULL,
        login VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        location_id INTEGER NOT NULL,
        api_user_id INTEGER NOT NULL,
        FOREIGN KEY (location_id) REFERENCES Location (id) ON DELETE CASCADE,
        FOREIGN KEY (api_user_id) REFERENCES api_user (id) ON DELETE CASCADE
    );
    """

    with db.atomic():
        db.execute_sql(create_location_table)
        db.execute_sql(create_user_table)
        db.execute_sql(create_device_table)
        print("Migrations are run")


create_tables()
