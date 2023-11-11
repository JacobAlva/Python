import logging

# create your custome logger with getLogger() function
logger = logging.getLogger(__name__)
logger.propagate = False        #stops default propagation
logger.info('Hello from helper.')
