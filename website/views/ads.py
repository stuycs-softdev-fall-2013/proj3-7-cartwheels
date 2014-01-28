from flask import render_template, request
from bson import ObjectId
from website.views.utils import base_context


def ads_page():
    context = base_context()
    return render_template('ads.html', **context)


def purchase_ad(name):
    context = base_context()
    return render_template('buyAd%s.html' % name.title(), **context)
