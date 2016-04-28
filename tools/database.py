from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# The engine tha app will use
__engine = create_engine('sqlite:///:memory:', echo=True)

# Manages the sessions for the whole app
__AppSession = sessionmaker(bind=__engine)

# Holds all the models once initialized
Base = declarative_base()

def get_app_session():
	return __AppSession()

def get_engine():
	return __engine