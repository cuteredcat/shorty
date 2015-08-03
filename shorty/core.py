#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for
from flask.ext.mongoengine.wtf import model_form

from StringIO import StringIO
from qrcode import make as qrmake
from qrcode.image.svg import SvgImage
from random import randint
from short_url import encode_url

from shorty import db
from shorty.models import Links

# create blueprint
core = Blueprint("core", __name__, template_folder="templates")

# create form for Links document
LinkForm = model_form(Links)

@core.route("/", methods=['POST', 'GET'])
def index():
    form = LinkForm(request.form)

    if request.method == "GET" and request.args.items():
        key, value = request.args.items()[0]
        if key:
            link = Links.objects.get_or_404(short=key)
            return render_template("redirect.html", link=link)

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
                return redirect(url_for("core.info", short=form.short.data))
            except db.NotUniqueError:
                form.short.errors.append('Duplicated short name.')

    return render_template("index.html", form=form)

@core.route("/info/<string:short>/")
def info(short):
    link = Links.objects.get_or_404(short=short)
    return render_template("info.html", link=link)

@core.route("/qr/<string:short>/")
def qr(short):
    stream = StringIO()

    qrmake(
        '%s?%s' % (url_for("core.index", _external=True), short),
        image_factory=SvgImage
    ).save(stream)

    return stream.getvalue().encode("utf-8"), 200, {
        "Content-Type": "image/svg+xml"
    }
