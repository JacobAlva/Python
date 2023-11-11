import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.critical('This is a critical message')
logging.debug('This is a debug message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.info('This is an info message')