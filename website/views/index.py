from flask import render_template, request
from utils import base_context
from website import photos
import random


# Index page
def index():
    context = base_context()
    imagelist = photos.find(is_cart=True)
    random.shuffle(imagelist)
    context['imagelist'] = imagelist
    return render_template('index.html', **context)


def search_results():
    context = base_context()
    context['keywords'] = request.args.get('kwds', '')
    context['location'] = request.args.get('loc', '')
    return render_template('results.html', **context)
