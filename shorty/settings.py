#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 5000

BASE_URL = "http://localhost:5000"
PREFIX = "_"

DEBUG = True
TESTING = False

SECRET_KEY = "DuMmY sEcReT kEy"

CSRF_ENABLED = True
CSRF_SESSION_KEY = "_csrf_token"

MONGODB_SETTINGS = {
    "db": "shorty",
    "host": "mongodb://localhost"
}

# import local settings if available

try:
    from .local_settings import *
except ImportError:
    pass
