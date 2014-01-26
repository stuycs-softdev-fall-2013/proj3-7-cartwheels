from flask import session, request
from bson import ObjectId
from website import api_key, users, carts, reviews, models, photos
from website.settings import DIST_OFFSET
import json, urllib, urllib2, re


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


# Get carts near a certain location
def get_carts_near(address, offset, number, search_object={}):
    # Geocode an address using a google maps api
    data = urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?api_key%s&sensor=false&address=%s' % (api_key, urllib.quote(address)))
    data = json.loads(data.read())
    geometry = data['results'][0]['geometry']
    results = []

    # Find all results within certain bounds
    try:
        box = []

        if geometry.has_key('bounds'):
            ne = geometry['bounds']['northeast']
            sw = geometry['bounds']['southwest']

            if ne['lat'] - sw['lat'] > DIST_OFFSET \
                    and ne['lng'] - sw['lng'] > DIST_OFFSET:
                box = [ [sw['lat'], sw['lng']], [ne['lat'], ne['lng']] ]

        if box == []:
            loc = geometry['location']
            box = [ [loc['lat'] - DIST_OFFSET, loc['lng'] - DIST_OFFSET],
                    [loc['lat'] + DIST_OFFSET, loc['lng'] + DIST_OFFSET] ]

        results += carts.within(box, offset, number, **search_object);

    except ValueError:
        pass

    return results


# Search for items using regex find
def search(item_type, offset, number, keywords, location):
    objs = []

    # Change objs depending on item type
    if item_type == 'cart':
        # Get results for each keyword
        for word in keywords:
            if word == '':
                continue

            # Check each text field
            for tfield in carts.text_fields():
                kwd = re.compile(r'(?: |^)' + word + '(?: |$)', re.IGNORECASE)
                search_object = {tfield: kwd}

                if len(objs) == 0:
                    if location != '':
                        objs += get_carts_near(location, offset, number,
                                search_object)

                    else:
                        objs += carts.find(offset, number, **search_object)

        # If there are no keywords, use location instead
        if len(objs) == 0 and keywords[0] == '' and len(keywords) == 1:
            objs += get_carts_near(location, offset, number)

    elif item_type == 'review':
        for word in keywords:
            for tfield in reviews.text_fields():
                kwd = re.compile(r'(?: |^)' + word + '(?: |$)', re.IGNORECASE)
                search_object = {tfield: kwd}
                objs += reviews.find(**search_object)

    return objs


# Serves the data from the backend to the frontend js using json module
def serve_data():
    item_type = request.args.get('item_type', None)
    keywords = urllib.unquote(request.args.get('keywords')).split(' ')
    location = request.args.get('location', '')
    offset = int(request.args.get('offset', 0))
    number = int(request.args.get('number', 20))

    objs = search(item_type, offset, number, keywords, location)
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
