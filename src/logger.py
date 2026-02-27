import os
import sys
import logging
from datetime import datetime

#.log format for saving logfile
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#log folder will be created if not exist and save logs in the logs folder
#log_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
#os.makedirs(log_path, exist_ok=True)
#getcwd function return current working directory and join function is used to join the path of logs folder and log file name to create the complete path for log file.

log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(log_path, exist_ok= True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)