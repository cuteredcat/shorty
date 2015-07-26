#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask.ext.mongoengine.wtf import model_form

from shorty.models import Users, Links

# create blueprint
admin = Blueprint("admin", __name__, template_folder="templates")

# create form for Users document
UserForm = model_form(Users)

# create form for Links document
LinkForm = model_form(Links)

@admin.route("/admin/")
def index():
    links = Links.objects.all()
    return render_template("admin/index.html", links=links)
