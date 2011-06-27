# used this code as a base
# http://code.google.com/p/django-axes/
from django.conf import settings

VERSION = (0, 0, 4, '')

def get_version():
    return '%s.%s.%s-%s' % VERSION

import logging, os


AUTHLOG_SAVE_GOOD_LOGINS=getattr(settings, 'AUTHLOG_SAVE_GOOD_LOGINS', True)
AUTHLOG_SAVE_BAD_LOGINS=getattr(settings, 'AUTHLOG_SAVE_BAD_LOGINS', False)

AUTHLOG_LOG_TO_FILE=getattr(settings, 'AUTHLOG_LOG_TO_FILE', False)
AUTHLOG_LOGDIR=getattr(settings, 'AUTHLOG_LOGDIR', '')
AUTHLOG_FILENAME=getattr(settings, 'AUTHLOG_FILENAME', 'authlog.log')
AUTHLOG_LOGGER=getattr(settings, 'AUTHLOG_LOGGER', 'authlog.watch_login')

AUTHLOG_TRACKED_MODELS=getattr(settings,'AUTHLOG_TRACKED_MODELS',['authlog.Access','authlog.AccessPage'])

AUTHLOG_SAVE_LOGIN_POST_DATA=getattr(settings,'AUTHLOG_SAVE_LOGIN_POST_DATA',True) 
AUTHLOG_SAVE_VIEW_POST_DATA=getattr(settings,'AUTHLOG_SAVE_VIEW_POST_DATA',True)


if AUTHLOG_LOG_TO_FILE:
    LOGFILE = os.path.join(AUTHLOG_LOGDIR, AUTHLOG_FILENAME)

    logging.basicConfig(level=logging.DEBUG,
			format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
			datefmt='%a, %d %b %Y %H:%M:%S',
			filename=LOGFILE,
			filemode='w')


    fileLog = logging.FileHandler(LOGFILE, 'w')
    fileLog.setLevel(logging.DEBUG)

    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')

    # tell the handler to use this format
    fileLog.setFormatter(formatter)

    # add the handler to the root logger
    #logging.getLogger('').addHandler(fileLog)


