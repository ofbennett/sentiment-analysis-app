import pathlib
import os

ROOT = pathlib.Path(__file__).resolve().parent.parent

class Config:
    DEBUG = False
    SERVER_PORT = 5000
    SERVER_HOST = '0.0.0.0'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    SERVER_PORT: os.getenv('SERVER_PORT', '5000')
    SERVER_ADDRESS: os.getenv('SERVER_ADDRESS', '0.0.0.0')