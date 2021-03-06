#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is shorty config file
# Do not change this file, use instance/shorty.conf instead

HOST = "localhost"
PORT = 5000

BASE_URL = "http://localhost:5000"

DEBUG = True
TESTING = False

SECRET_KEY = "DuMmY sEcReT kEy"

CSRF_ENABLED = True
CSRF_SESSION_KEY = "_csrf_token"

MONGODB_SETTINGS = {
    "db": "shorty",
    "host": "mongodb://localhost"
}

BABEL_DEFAULT_LOCALE = "en"

SHORTY_NAME = "Shorty"
SHORTY_PROVIDER = "Shorty"

LINKS_PER_PAGE = 50

# Google Analytics
GA_UA = "UA-XXXXXXXX-X"
