#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask.ext.mongoengine.wtf import model_form

from shorty.models import Users, ShortLinks

# create blueprint
admin = Blueprint("admin", __name__, template_folder="templates")

@admin.route("/admin/")
def index():
    return render_template("admin/index.html")
