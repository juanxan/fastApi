from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'juanxan1'
POSTGRES_DB = 'inventario'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5432

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Session= sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
