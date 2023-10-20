from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DBNAME = os.getenv('POSTGRES_DB')
SECRET_MANAGER = os.getenv('SECRET_MANAGER')
SECRET_JWT = os.getenv('SECRET_JWT')
