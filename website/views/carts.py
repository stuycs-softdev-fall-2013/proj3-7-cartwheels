from flask import render_template, request
from bson import ObjectId
from website import carts, reviews, photos
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
            context['error'] = 'You\'ve already written a review for this cart'

    return render_template('cart.html', **context)


def menu_page(cid):
    context = base_context()
    context['cart'] = carts.find_one(_id=ObjectId(cid));

    if request.method == 'POST':
        form = request.form
        tags = [t.strip() for t in form['tags'].split(',')]
        image = ''

        if request.files.has_key('file'):
            try:
                f = request.files['file']
                image = photos.insert(image_file=f, is_cart=False, is_default=False, title=form['name'])

            except IOError:
                print "error"

        menu_item = {'name': form['name'], 'price': form['price'], 'tags': tags, 'image': image.url_path}
        context['cart'].add_menu(menu_item)

    return render_template('menu.html', **context)


def directions(cid):
    context = base_context()
    context['cart'] = carts.find_one(_id=ObjectId(cid));

    return render_template('directions.html', **context)
