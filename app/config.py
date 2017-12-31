import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.environ['POSTGRES_URL']

class ProductionConfig(Config):
  DEBUG = False


class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True


class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True


class TestingConfig(Config):
  TESTING = True
