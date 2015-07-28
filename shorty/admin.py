#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for
from flask.ext.mongoengine.wtf import model_form

from random import randint
from short_url import encode_url

from shorty import db
from shorty.models import Users, Links

# create blueprint
admin = Blueprint("admin", __name__, template_folder="templates")

# create form for Users document
UserForm = model_form(Users)

# create form for Links document
LinkForm = model_form(Links)

@admin.route("/admin/", methods=["POST", "GET"])
def index():
    form = LinkForm(request.form, exclude=['created_at', 'tags'])
    tags = []

    if request.method == "POST":
        # grub tags
        # TODO: find better way to save tags
        tags = [tag.strip() for tag in request.form.get("tags", "").split(",") if tag.strip()]

        if form.full.validate(form) and not form.short.data:
            # auto create new short name
            # TODO: find better solution for custom url creation
            form.short.data = encode_url(randint(1, 1000000000000))
            while Links.objects.filter(short=form.short.data):
                form.short.data = encode_url(randint(1, 1000000000000))

        if form.validate():
            try:
                link = form.save()

                # save tags
                link.tags = tags
                link.save()

                return redirect(url_for("admin.index"))
            except db.NotUniqueError:
                form.short.errors.append('Duplicated short name.')

    links = Links.objects.paginate(page=1, per_page=50)
    return render_template("admin/index.html", form=form, tags=tags, links=links)
