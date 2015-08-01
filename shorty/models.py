#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from shorty import db

class Users(db.Document):
    username = db.StringField(max_length=255, required=True, unique=True)
    password = db.StringField(max_length=64, required=True)
    email = db.EmailField(unique=True)

class Links(db.Document):
    created_at = db.DateTimeField(default=datetime.now, required=True)
    full = db.URLField(required=True)
    short = db.StringField(max_length=255, required=True, unique=True)
    comment = db.StringField()
    tags = db.ListField(db.StringField(max_length=30))

    meta = {
        'indexes': ['-created_at', 'tags'],
        'ordering': ['-created_at']
    }
