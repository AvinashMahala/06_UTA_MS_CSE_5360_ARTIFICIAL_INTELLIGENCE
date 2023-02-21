'''
This code sets up the logging configuration to include the timestamp, log level, and log message. The log function can be used to log messages at the desired log level (e.g., log("some message", logging.DEBUG)). The log level can be set to any of the following values (in order of increasing severity): DEBUG, INFO, WARNING, ERROR, and CRITICAL.
'''

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)


def log(msg, level=logging.DEBUG):
    logging.log(level, msg)
