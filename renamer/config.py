#init-document
import os
from dotenv import load_dotenv

#Preparing Enviorment#
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, '.env'))

#INDICATE IF THIS APP, SHOULD BE HAS DEBUG
DEBUG = True if os.getenv('DEBUG', False) == 'True' else False

#APPLICATION ENVIORMENT VARIABLES ()
API_ROOT = os.getenv('API_ROOT')
API_USERNAME = os.getenv('API_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD')
WAIT_TIME = os.getenv('WAIT_TIME', 60)
MAX_RETRIES = os.getenv('MAX_RETRIES', 60)
RETRY_AT = os.getenv('RETRY_AT', 15)
