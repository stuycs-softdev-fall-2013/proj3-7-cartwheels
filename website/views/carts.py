from flask import render_template
from bson import ObjectId
from website import carts
from website.views.utils import base_context


# Cart page
def cart_page(cid):
    context = base_context()
    context['cart'] = carts.find_one(_id=ObjectId(cid));
    return render_template('cart.html', **context)


# Manage carts
def manage_cart(cid):
    context = base_context()
    context['cart'] = carts.find_one(_id=ObjectId(cid));
    return render_template('manage.html', **context)


# Review
def review(cid):
    context = base_context()
    context['cart'] = carts.find_one(_id=ObjectId(cid));
    return render_template('review.html', **context)
