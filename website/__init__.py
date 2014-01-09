from flask import Flask
from website.settings import SECRET_KEY, STORE_FILE
from website.models import Collection, Cart, User, Review


app = Flask(__name__)
app.secret_key = SECRET_KEY

models = Collection()
carts = Cart()
users = User()
reviews = Review()

f = open(STORE_FILE)
api_key = f.readlines()[0].strip()
f.close()


import website.views
