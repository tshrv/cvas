from .base import *

LOG_STREAM_HANDLER_ENABLED = True
LOG_FILE_NAME = 'app.log'
LOG_FILE_DIR = ROOT_DIR
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)

TWILIO_ENABLED = False
