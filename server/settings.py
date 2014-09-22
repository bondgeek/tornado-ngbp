__author__ = 'bondgeek'

import os
import inspect

ENVIRONMENT = os.environ.get('ENVIRONMENT', "staging")

CLIENT_BUILD_PATH = {
    'staging': 'build',
    'prod': 'bin',
}.get(ENVIRONMENT, "build")

BASE_PATH = os.path.realpath(
    os.path.join(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]), '../')
)
# path to angularjs app
CLIENT_PATH = os.path.realpath(os.path.join(BASE_PATH, 'client', CLIENT_BUILD_PATH))
# path to static page templates (errors, etc.)
TEMPLATE_PATH = os.path.realpath(os.path.join(BASE_PATH, 'client', 'shared', 'templates'))
STATIC_PATH = os.path.realpath(os.path.join(BASE_PATH, 'client', CLIENT_BUILD_PATH))

TEMPLATE_GLOBAL_ENV = {}
COOKIE_USER_ID_NAME = ""
COOKIE_NAME = ""
COOKIE_EXPIRE_DAYS = 1
