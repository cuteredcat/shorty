#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is shorty config file
# Do not change this file, use instance/shorty.conf instead

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

BABEL_DEFAULT_LOCALE = "en"
