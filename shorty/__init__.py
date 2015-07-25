#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.mongoengine import MongoEngine

from shorty import settings
from shorty.core import core
from shorty.admin import admin

# init application
app = Flask("shorty")
app.config.from_object(settings)

# init db
db = MongoEngine(app)

# register blueprints
app.register_blueprint(core)
app.register_blueprint(admin)

if __name__ == "__main__":
    app.run()
