from . import Config

class Production(Config):
    DB_URL='sqlite:///config/db/production.db'