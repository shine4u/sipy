# -*- coding: utf-8 -*-

import sys, time, os, re, shutil, logging, smtplib
from email.Utils import COMMASPACE, formatdate
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

''' logging interface
we use logging module in python lib.
'''
GLB_LOG = None

