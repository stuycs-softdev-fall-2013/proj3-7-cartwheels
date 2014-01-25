# Models and Collections for carts
from website.models.base import Collection, Model
from website.models.review import Review
from website.models.tag import Tag
from website.models.photo import Photo


reviews = Review()
tags = Tag()
photos = Photo()


''' Format for an insert would be:
    carts.insert(lat=...,lng=...,address=...,zip_code=...,
        borough=...,name=...)
'''
class CartModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(CartModel, self).__init__(db, fs, collection, obj)
        self.url_path = '/carts/%s' % str(self.get_id())
        self.save()

    # Adds image associated with the cart
    def add_image(self, image_file, label):
        img = photos.insert(image_file=image_file, is_cart=True, cart_id=self.get_id(), label=label)
        self.image_paths += img.url_path
        self.save()
        return img

    # Get images associated with cart
    def get_images(self, **kwargs):
        return photos.find(cart_id=self.get_id(), **kwargs)

    # Adds tag to cart
    def add_tag(self, label):
        t = tags.find_one(label=label)

        if not t:
            t = tags.insert(label=label)

        if not any(s == label for s in self.tags):
            t.count += 1
            t.save()
            self.tags.append(label)
            self.save()

        return t

    # Adds a review under the users page
    def add_review(self, user, **kwargs):
        rev = reviews.insert(cart_id=self.get_id(), user=user, **kwargs)
        ratings = [r.rating for r in self.get_reviews()]
        self.rating = float(sum(ratings)) / float(len(ratings))
        self.review_ids += rev.get_id()
        self.save()
        return rev

    # Get reviews made by this user, and with other arguments
    def get_reviews(self, **kwargs):
        return reviews.find(cart_id=self.get_id(), **kwargs)


    # Def add menu
    def add_menu(self, menu):
        self.menu += menu
        self.save()


class Cart(Collection):

    def __init__(self):
        super(Cart, self).__init__(CartModel)

    def insert(self, **kwargs):
        return super(Cart, self).insert(tags=[], review_ids=[], image_paths=[],
                rating=None, url_path='', menu=[], **kwargs)

    # Get by tag function
    def get_by_tag(self, label):
        return [item for item in self.find() if label in item.tags]

    # Names of cart text fields (for searching)
    def text_fields(self):
        return ['name']

    # Names of cart location fields (for searching)
    def location_fields(self):
        return ['address', 'borough', 'zip_code']
