import logging,logging.handlers

def setupLog():
    logger = logging.getLogger('a')
    logger.setLevel(logging.INFO)
    logfilename = 'log.log'
    handler = logging.handlers.RotatingFileHandler(logfilename,maxBytes = 50000,backupCount = 5) 
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
