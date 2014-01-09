from flask import render_template
from utils import base_context


# Index page
def index():
    context = base_context()
    return render_template('index.html', **context)
