from flask import session, request
from bson import ObjectId
from website import app, api_key, users, carts, reviews, models
import json


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


# Serves the data from the backend to the frontend js using json module
@app.route('/_data')
def serve_carts():
    # Get iterable copy of args
    item_type = request.args.get('item_type')
    rargs = request.args.copy()
    kwargs = {}

    # Copy request args into a copy
    for k in rargs.keys():
        if k != 'item_type':
            kwargs[k] = rargs[k]

        if '_id' in k:
            kwargs[k] = ObjectId(rargs[k])

    # Change objs depending on item type
    objs = carts.find(**kwargs)
    if item_type == 'review':
        objs = reviews.find(**kwargs)

    results = [o._obj for o in objs]

    # Remove incompatible types
    for r in results:
        serialize(r)

    # Return results as an array
    data = {'results': results}
    return json.dumps(data)


# Get image by id
@app.route('/_image/<image_id>')
def serve_image(image_id):
    image = models.fs.get(ObjectId(image_id))
    data = image.read()
    image.close()
    return data
