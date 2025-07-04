import psycopg2
from config import load_config


def connect(config):

    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Bro, you just connected to your Database.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)
