import os
import sys
import logging
from datetime import datetime

#.log format for saving logfile
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

#log folder will be created if not exist and save logs in the logs folder
log_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)


#tell at what level we want to log and the format of the log message
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)

'''
if __name__ == "__main__":
    logging.info("Logging has started.")
    '''