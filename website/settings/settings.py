# Application
SECRET_KEY = "}. 2}MpuI3J[yYGg8*b9jL&;%Lyt(WhxxhlFaoadm}sQjaVF+/z`vs~#qd@ Spd8"
STORE_FILE = "website/settings/store.info"

# Mongodb
DB_NAME = 'cartwheels'
COLLECTIONS = {
        'User': 'users',
        'Cart': 'carts',
        'Tag': 'tags',
        'Review': 'reviews',
        'Photo': 'photos',
        'CartAd': 'ads',
        'Collection': 'ignore'
        }

IGNORE_ATTRS = ['_obj', 'collection', 'fs', 'db']
