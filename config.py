import os


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PROPAGATE_EXCEPTIONS = True
    _MYSQL_DRIVER = "mysql+pymysql://"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "password"
    MYSQL_ENDPOINT = "localhost"
    MYSQL_DBNAME = "nanonetsdev"
    SQLALCHEMY_DATABASE_URI = BaseConfig._MYSQL_DRIVER + MYSQL_USERNAME + ":" + MYSQL_PASSWORD + "@" + MYSQL_ENDPOINT + "/" + MYSQL_DBNAME


class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME', 'invalid')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'invalid')
    MYSQL_ENDPOINT = os.getenv('MYSQL_ENDPOINT', 'invalid')
    MYSQL_DBNAME = "nanonets"
    SQLALCHEMY_DATABASE_URI = BaseConfig._MYSQL_DRIVER + MYSQL_USERNAME + ":" + MYSQL_PASSWORD + "@" + MYSQL_ENDPOINT + "/" + MYSQL_DBNAME


def get_config():
    config_name = os.getenv('FLASK_CONFIGURATION', 'prod')
    if config_name == 'dev':
        return DevelopmentConfig
    else:
        return ProdConfig
