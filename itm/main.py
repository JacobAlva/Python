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
"""

# for troblueshooting
try:
    a = [1,2,3]
    val = a[4]  # returns a value error
except IndexError as e:
    logging.error(e, exc_info = True)