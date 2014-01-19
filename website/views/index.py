from flask import render_template
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
