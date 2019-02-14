"""Configuration Classes"""
import os
class Config(object):
    """ Main configurations class """
    DEBUG = False
class Development(Config):
    """ Development configurations are put here """
    DEBUG = True
    DATABASE_URI = os.getenv('DATABASE_URL','')

class Testing(Config):
    """ The configurations for testing """
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.getenv('DATABASE_TEST_URL', '')
class Production(Config):
    """ The configurations for production """
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv("DATABASE_PROC_URL",'')
    
app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
}