"""sqlalchemy.py

Provides sqlalchemy connection utilities.
"""
import os

#pylint: disable=import-error
from sqlalchemy import create_engine
#pylint: enable=import-error

def get_engine(isolation_level="REPEATABLE READ"):
    """get_engine returns connection string for mysql+pymysql"""
    user = os.environ.get('POSTGRES_USER')
    pword = os.environ.get('POSTGRES_PASSWORD')
    host = os.environ.get('POSTGRES_HOST')
    database = os.environ.get('POSTGRES_DB')

    base = f'{user}:{pword}@{host}:5432/{database}'
    url = f'postgresql+psycopg2cffi://{base}'
    return create_engine(
        url,
        isolation_level=isolation_level,
        pool_size=20,
        max_overflow=10,
        pool_pre_ping=True
    )
