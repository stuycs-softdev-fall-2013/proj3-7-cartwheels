from flask import render_template
from website import app
from utils import base_context


# Base function, renders the template with the api key as input
@app.route('/')
def home():
    context = base_context()
    return render_template('index.html', **context)
