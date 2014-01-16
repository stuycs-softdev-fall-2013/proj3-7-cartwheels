from flask import render_template
from utils import base_context
from website.models import Photo
import random


photos = Photo()


# Index page
def index():
    context = base_context()
    imagelist = photos.find(is_cart=True)
    random.shuffle(imagelist)
    context['imagelist'] = imagelist
    return render_template('index.html', **context)
