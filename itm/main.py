import logging

"""
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s', datefmt='%m/%d/%Y %H:%M:%S')

#logger.propagate = false
'''
logging.critical('This is a critical message')
logging.debug('This is a debug message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.info('This is an info message')
'''
# this would import the logger from the helper module and print out the default logging details.
''' Creating this logger from helper creates an hierarchy of loggers starting at the root logger.
    All the other loggers get added to the heirarchy and propagate to the base logger by default.
    To disable propagation, set it to "False" in the helper file.
'''
import helper

# HANDLERS
'''Handler objects are responsible for dispensing the appropriate block message to the handlers specific location for the objects'''

logger = logging.getLogger(__name__)        # create logger in the module

# create handler
stream_h = logging.StreamHandler()              # logs to stream
file_h = logging.FileHandler('file.log')        # logs to file

# set level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# specify formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add handler to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

# testing the logger/handler
logger.warning('This is a warning')
logger.error('This is an error')


# added configuration
''' For added configuration, a config file will be created (logging.conf) and imported into the project.
    This makes logging easier as you don't have to hardcode it or modify your code to fit it in.'''

import logging.config
#logging.config.fileConfig('logging.conf')

# you can also use a dictconfig instead of a fileConfig
logging.config.dictConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('This is a debug message')


# for troblueshooting
import traceback
try:
    a = [1,2,3]
    val = a[4]  # returns a value error
except: # IndexError as e: cover for everything
    # logging.error(e, exc_info=True)
    logging.error("The error is %s", traceback.format_exc())
"""

# ROTATING FILE HANDLER
# log to file
#from logging.handlers import RotatingFileHandler

# if the app will be running for a long time, you can use a timedRotatingFileHandler
# that logs after a specific amount of time
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB and keep backup loggs app.log.1, app.log.2, etc
#handler = RotatingFileHandler('app.log', maxBytes = 2000, backupCount = 5)
#logger.addHandler(handler)

#for _ in range (1000):          # _ means you don't care about it, for anything in range (1000)
#    logger.info('Hello, world!')

# s-secs, m-mins, h, d, midnight, w0-Monday, w1-Tuesday, etc.
handler = TimedRotatingFileHandler('timed_test.log', when = 's', interval = 5, backupCount = 5)

for _ in range (6):          # _ means you don't care about it, for anything in range (1000)
    logger.info('Hello, world!')
    time.sleep(5)       # wait 5 secs, then log again.


# if you are logging a lot of files, it is preferrable to log in json format using the
# Python JSON logger library on GitHub