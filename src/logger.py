import os
from datetime import datetime

def log(data):
    LOG_DIRECTORY = "./../log"
    LOG_PATH = LOG_DIRECTORY + "/log.log"

    log_str = "[" + datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + "]" + data

    if not os.path.exists(LOG_DIRECTORY):
		os.makedirs(LOG_DIRECTORY)
    
    with open(LOG_PATH, 'a+') as log_file:
		log_file.write(log_str + "\n")

    print log_str 