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

@admin.route("/admin/", methods=["POST", "GET"])
def index():
    form = LinkForm(request.form)

    if request.method == "POST":
        if form.full.validate(form) and not form.short.data:
            # auto create new short name
            # TODO: find better solution for custom url creation
            form.short.data = encode_url(randint(1, 1000000000000))
            while Links.objects.filter(short=form.short.data):
                form.short.data = encode_url(randint(1, 1000000000000))

        if form.validate():
            try:
                form.save()
                return redirect(url_for("admin.index"))
            except db.NotUniqueError:
                form.short.errors.append('Duplicated short name.')

    links = Links.objects.paginate(page=1, per_page=50)
    return render_template("admin/index.html", links=links)
