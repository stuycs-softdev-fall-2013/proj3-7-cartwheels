from flask import render_template, request
from bson import ObjectId
from website import carts, reviews
from website.views.utils import base_context


# Cart page
def cart_page(cid):
    context = base_context()
    context['cart'] = carts.find_one(_id=ObjectId(cid));
    context['reviews'] = context['cart'].get_reviews()

    if request.method == 'POST':
        form = request.form
        cart = context['cart']
        tags = [t.strip() for t in form['tags'].split(',')]

        if reviews.find_one(user=context['user'].username,
                cart_id=cart.get_id()) is None:
            cart.add_review(context['user'].username, text=form['review'],
                    rating=int(form['rating']))
            cart.tags += tags
            cart.save()

        else:
            context['error'] = 'You already wrote a review for this cart'

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
