# -*- coding: utf-8 -*-

import sys, time, os, re, shutil, logging, smtplib
from email.Utils import COMMASPACE, formatdate
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

''' logging interface
we use logging module in python lib.
'''

''' init log, call at main thread.
'''
def init_log(**kwargs):
    modname  = kwargs.get('modname', 'default')
    logfile  = kwargs.get('logfile', 'stderr')
    isdebug = True if ('isdebug' in kwargs and kwargs['isdebug'] == True) else False
    loglevel = logging.DEBUG if isdebug else logging.INFO
    logger = logging.getLogger(modname)
    if isdebug: logger.setLevel(loglevel)
    fh = logging.StreamHandler() if logfile == 'stderr' else logging.FileHandler(logfile)
    fh.setLevel(loglevel)
    formatter = logging.Formatter('%(levelname)-8s %(asctime)s %(filename)14s:%(lineno)-.3d - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def close_debug(logger):
    logger.setLevel(logging.INFO)
def open_debug(logger):
    logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    logger = init_log(isdebug = False)
    logger.debug('isdebug=false, you cannot see me.')
    logger.info('isdebug=false, you can see me.')
    logger.warn('isdebug=false, you can see me.')

    open_debug(logger)
    logger.debug('isdebug=true, you can see me.')
    logger.info('isdebug=false, you can see me.')
    logger.warn('isdebug=false, you can see me.')
