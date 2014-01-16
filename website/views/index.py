from flask import render_template
from utils import base_context
from os import listdir


image_path = '/Users/benjaminattal/dev/softdev/projects/cartwheels/website/static/images'
imagelist = ['images/%s' % f for f in listdir(image_path) if f not in ['.DS_Store', 'search-icon.png']]


# Index page
def index():
    context = base_context()
    context['imagelist'] = imagelist
    return render_template('index.html', **context)
