import os
from dotenv import load_dotenv

directoryname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(directoryname, '..', '.env'))
except FileNotFoundError:
    pass

SCORES_FILENAME = os.getenv('SCORES_FILENAME') or 'scores.csv'
SCORES_FILE_PATH = os.path.join(directoryname, '..', 'data', SCORES_FILENAME)
