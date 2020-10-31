##########################################################################
# Project         : NTT ASSIGNMENT
# Title           : logger_creation.py
# Description     : This file set ups logging file handler
# Author          : ANIL GOUD CHERUKU
# Date            : 30-Oct-2020
# Version         : 1.0.0
# Python_version  : 3.6.3
##########################################################################
# Importing all packages required for this script
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_file, level=logging.DEBUG):
    """

    :param log_file: log file name
    :param level: Level of Logging : INFO|DEBUG|ERROR|WARNING

    """
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(process)d - %('
                                  'levelname)s - (%(lineno)d) - %(message)s')

    # create file and console handlers
    rf_handler = RotatingFileHandler(log_file, mode='a',
                                     maxBytes=10485760,
                                     backupCount=90, encoding=None,
                                     delay=0)
    rf_handler.setLevel(level)
    rf_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logging.basicConfig(handlers=[console_handler, rf_handler],
                        level=logging.DEBUG, format=formatter)
