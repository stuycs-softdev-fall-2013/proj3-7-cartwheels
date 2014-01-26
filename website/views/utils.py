from flask import session, request
from bson import ObjectId
from website import api_key, users, carts, reviews, models, photos
import json, urllib, re


def base_context():
    context = {}
    context['API_KEY'] = api_key
    context['user'] = None

    if 'username' in session:
        context['user'] = users.find_one(username=session['username'])

    return context


def serialize(obj):
    for k in obj:
        try:
            json.dumps(obj[k])
        except TypeError:
            if type(obj[k]) == dict:
                serialize(obj[k])
            elif type(obj[k]) == list:
                for i in obj[k]:
                    serialize(i)
            else:
                obj[k] = str(obj[k])


# Search for items using regex find
def search(item_type, keywords, location):
    objs = []

    # Change objs depending on item type
    if item_type == 'cart':

        for word in keywords:

            for tfield in carts.text_fields():
                kwd = re.compile(r'(?: |^)' + word + '(?: |$)', re.IGNORECASE)
                search_object = {tfield: kwd}
                location_fields = carts.location_fields()

                if location != '':

                    for lfield in location_fields:
                        loc = re.compile(r'(?: |^)' + location + '(?: |$)', re.IGNORECASE)
                        search_object[lfield] = loc
                        objs += carts.find(**search_object)

                        search_object.pop(lfield, None)

                if len(objs) == 0:
                    objs += carts.find(**search_object)

    elif item_type == 'review':

        for word in keywords:

            for tfield in reviews.text_fields():
                kwd = re.compile(r'(?: |^)' + word + '(?: |$)', re.IGNORECASE)
                search_object = {tfield: kwd}
                location_fields = carts.location_fields()
                objs += reviews.find(**search_object)

    return objs


# Serves the data from the backend to the frontend js using json module
def serve_data():
    item_type = request.args.get('item_type', None)
    keywords = urllib.unquote(request.args.get('keywords')).split(' ')
    location = request.args.get('location', '')

    objs = search(item_type, keywords, location)

    results = [o._obj for o in objs]

    # Remove incompatible types
    for r in results:
        serialize(r)

    # Return results as an array
    data = {'results': results}
    return json.dumps(data)


# Get image by id
def serve_image(image_id):
    image = models.fs.get(ObjectId(image_id))
    data = image.read()
    image.close()
    return data


# Default image
def serve_default():
    # serve a default image
    img = photos.find_one(is_default=True)
    return img.read()
