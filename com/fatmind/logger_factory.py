'''
Created on 2013-1-30

@author: bohan.sj
'''

import logging

class LoggerFatory:
    '''
    create log obj
    '''
     
    def getLogger(self, logger_name):   
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s")
        fileHandler = logging.FileHandler("logs.txt")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        consoleHandle = logging.StreamHandler()
        consoleHandle.setFormatter(formatter)
        logger.addHandler(consoleHandle)
        return logger