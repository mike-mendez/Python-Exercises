from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:thisismyr00tpassword!@localhost/todoapp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLite3
# SQLALCHEMY_DATABASE_URL = "sqlite3:////todos.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

