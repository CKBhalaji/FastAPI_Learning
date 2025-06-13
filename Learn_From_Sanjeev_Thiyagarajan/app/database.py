from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import Settings

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{Settings().database_username}:{Settings().database_password}@{Settings().database_hostname}:{Settings().database_port}/{Settings().database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Used for the database connection retry logic.
# while True:
#     try:
#         # Attempt to connect to the database
#         conn = psycopg.connect(host = "localhost",
#                                dbname = "fastapi",
#                                user = "postgres",
#                                password = "2003")
#         cursor = conn.cursor()
#         print("Database connection successful")
#         break  
#     except Exception as e:
#         print("Database connection failed")
#         print(f"Error: {e}")
#         time.sleep(2) 
#         break 