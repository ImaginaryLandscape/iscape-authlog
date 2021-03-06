Requires Django 1.7+
Supports Python 2.6+ to 3

## Install

0) Add Django admin urls:

    ...
    (r'^admin/', include(admin.site.urls)),
    ...

1) Add authlog to installed apps in settings.py

    INSTALLED_APPS = (
       ...
       'authlog',
       ...
    )


2) Add authlog to near beginning of middlware in settings.py

    MIDDLEWARE_CLASSES = (
        'authlog.logadminmiddleware.LogAdminMiddleware',
        ....
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    )

3) Configure AUTHLOG in settings.py.  Sane defaults exist.

- AUTHLOG_SAVE_GOOD_LOGINS = True or False (default True)
  Specify whether to log good logins

- AUTHLOG_SAVE_BAD_LOGINS = True or False (default False)
  Specify whether to log bad logins (login attempts)

- AUTHLOG_TRACKED_MODELS = (default is ['authlog.Access','authlog.AccessPage'] )
  Specify which models and apps to log views of.  Must be a list of 'app.model' names

- AUTHLOG_SAVE_LOGIN_POST_DATA = True or False (default True)
  Specify whether to save http POST data for logins to the db

- AUTHLOG_SAVE_VIEW_POST_DATA = True or False (default True)
  Specify whether to save http POST data for page views to the db


NOTE: These settings offer a simple interface to start logging.
Alternatively, using Django 1.3, you can simple define a logger
called authlog.watch_login within settings.py and it will
start logging to your custom logger.

- AUTHLOG_LOG_TO_FILE = True or False (default False)
  Specify whether to log to a file via python logging

- AUTHLOG_LOGDIR = path to log dir (default none - current dir)
  If LOG_TO_FILE set, specify what dir the file should log to

- AUTHLOG_FILENAME = log file name (default authlog.log)
  If LOG_TO_FILE set, specify the log file name



4) Migrate the database

    ./manage.py migrate



## MANAGEMENT COMMANDS

These two commands dump the Access and AccessPage tables stdout as CSV

    manage.py authlog_dumpview
    manage.py authlog_dumplogin
