from flask import render_template
from utils import base_context


# Base function, renders the template with the api key as input
def index():
    context = base_context()
    return render_template('index.html', **context)
