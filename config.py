import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Security key (OK for dev)
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key-change-later"

    # ✅ SQLite DB inside instance folder
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or "sqlite:///" + os.path.join(BASE_DIR, "instance", "urbannest.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
