from flask import render_template
from utils import base_context


# Cart page
def cart_page(cid=None):
    context = base_context()
    return render_template('cart.html', **context)


# Manage carts
def manage_cart(cid=None):
    context = base_context()
    return render_template('manage.html', **context)

