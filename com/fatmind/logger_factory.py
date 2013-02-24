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
        logger.setLevel(logging.WARN)
        formatter = logging.Formatter("%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s")
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
        return logger