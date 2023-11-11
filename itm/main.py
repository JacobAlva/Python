import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s', datefmt='%m/%d/%Y %H:%M:%S')

#logger.propagate = false
"""
logging.critical('This is a critical message')
logging.debug('This is a debug message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.info('This is an info message')
"""
# this would import the logger from the helper module and print out the default logging details.
''' Creating this logger from helper creates an hierarchy of loggers starting at the root logger.
    All the other loggers get added to the heirarchy and propagate to the base logger by default.
    To disable propagation, set it to "False" in the helper file.
'''
import helper
