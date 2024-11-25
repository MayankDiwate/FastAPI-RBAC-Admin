import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
CLIENT_URL = os.getenv("CLIENT_BASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

if not CLIENT_URL:
    CLIENT_URL = "http://localhost:5173"