#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for
from flask.ext.mongoengine.wtf import model_form

from shorty.models import Links

# create blueprint
core = Blueprint("core", __name__, template_folder="templates")

# create form for Links document
LinkForm = model_form(Links)

@core.route("/")
def index():
    form = LinkForm(request.form)
    if request.method == "POST" and form.validate():
        form.save()
        redirect(url_for("core.index"))

    return render_template("index.html", form=form)
