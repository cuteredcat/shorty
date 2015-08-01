#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, redirect, render_template, request, url_for
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
    formtags = []
    tags = []

    if request.method == "GET":
        tags = request.args.getlist("tags")

    if request.method == "POST":
        # grub tags
        # TODO: find better way to save tags
        formtags = [tag.strip() for tag in request.form.get("tags", "").split(",") if tag.strip()]

        # add admin tag, for links created from admin panel
        if not "admin" in formtags: formtags.append("admin")

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
                link.tags = formtags
                link.save()

                return redirect(url_for("admin.index"))
            except db.NotUniqueError:
                form.short.errors.append('This name already exists.')

    if tags and len(tags):
        links = Links.objects.filter(tags__in=tags).paginate(page=1, per_page=app.config["LINKS_PER_PAGE"])
    else:
        links = Links.objects.paginate(page=1, per_page=app.config["LINKS_PER_PAGE"])

    tagstree = Links.objects.all().distinct(field="tags")

    return render_template("admin/index.html",
      form=form,
      formtags=formtags,
      tagstree=tagstree,
      tags=tags,
      links=links
    )

@admin.route("/admin/page/<int:page>/")
def more(page):
    tags = []

    if request.method == "GET":
        tags = request.args.getlist("tags")

    if tags and len(tags):
        links = Links.objects.filter(tags__in=tags).paginate(page=page, per_page=app.config["LINKS_PER_PAGE"])
    else:
        links = Links.objects.paginate(page=page, per_page=app.config["LINKS_PER_PAGE"])

    return render_template("admin/more.html", links=links)

@admin.route("/admin/delete/<string:short>/")
def delete(short):
    link = Links.objects.get_or_404(short=short)
    link.delete()

    return jsonify(short=short, deleted=True)
