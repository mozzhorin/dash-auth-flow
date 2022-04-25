import configparser
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read("/app/dash/utilities/config.txt")

engine = create_engine(config.get('database', 'con'))