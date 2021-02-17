import os
# from dotenv import load_dotenv

# load_dotenv()


# Statement for enabling the development environment
DEBUG = True

# Define the application directory

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  


# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# Application threads. 
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True



#TODO: Figure out how to secure these 

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"


# Secret key for signing cookies
SECRET_KEY = "secret"



SQLALCHEMY_TRACK_MODIFICATIONS = False