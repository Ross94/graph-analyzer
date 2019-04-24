import os
import sys
from datetime import datetime

def log(data):
    '''Print data and save the same data in file whit date in UTC format.'''
    
    LOG_DIRECTORY = "./../log"
    LOG_PATH = LOG_DIRECTORY + "/log.log"

    log_str = "[" + datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + "] " + data

    if not os.path.exists(LOG_DIRECTORY):
      os.makedirs(LOG_DIRECTORY)
    
    with open(LOG_PATH, 'a+') as log_file:
      log_file.write(log_str + "\n")

    print(log_str) 

def progress_bar(msg, elem, total):
    '''Progress bar showed on terminal'''

    percentage = elem / total * 100
    sys.stdout.write('\r{0}, nodes calculated: {1}/{2}, percentage: {3:.6f}{4}'.format(msg, elem, total, percentage, "%"))
    if elem == total:
        sys.stdout.write('\n')
    sys.stdout.flush() 