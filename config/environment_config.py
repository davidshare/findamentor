import os
from .utils import get_env_vars

class Config:
  '''
    class with base configuration for the app
  '''
  SECRET_KEY = get_env_vars('SECRET_KEY')
  DEBUG = False
  DB_URL = get_env_vars('DB_DEV_URL')

class ProductionConfig(Config):
  '''
    class with configuration for the production environment
  '''
  DB_URL = get_env_vars('DB_PROD_URL')
  DB_NAME = get_env_vars('PROD_DB')

class DevelopmentConfig(Config):
  '''
    class with configuration for the development environment
  '''
  DEBUG=True
  DB_URL = get_env_vars('DB_DEV_URL')
  DB_NAME = get_env_vars('DEV_DB')

class TestConfig(Config):
  '''
    class with configuration for the test environment
  '''
  DB_URL = get_env_vars('DB_TEST_URL')
  DB_NAME = get_env_vars('TEST_DB')


config = {
    'development': DevelopmentConfig,
    'staging': ProductionConfig,
    'production': ProductionConfig,
    'testing': TestConfig
}
