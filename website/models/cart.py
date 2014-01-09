# Models and Collections for carts
from datetime import datetime
from website.models.base import Collection, Model
from website.models.review import Review
from website.models.tag import Tag
from website.models.photo import Photo


reviews = Review()
photos = Photo()


''' Format for an insert would be:
    carts.insert(lat=...,lng=...,address=...,zip_code=...,
        borough=...,name=...)
'''
class CartModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(CartModel, self).__init__(db, fs, collection, obj)

    # Adds image associated with the cart
    def add_image(self, image_file, label):
        image_id = self.fs.put(image_file.read())
        img = photos.insert(cart_id=self.get_id(), image_id=image_id,
                date_added=datetime.now(), label=label)
        return img

    # Get images associated with cart
    def get_images(self, **kwargs):
        return photos.find(cart_id=self.get_id(), **kwargs)

    # Adds tag to cart
    def add_tag(self, label):
        tags = Tag()
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
        self.save()
        return rev

    # Get blog reviews made by this user, and with other arguments
    def get_reviews(self, **kwargs):
        return reviews.find(cart_id=self.get_id(), **kwargs)


class Cart(Collection):

    def __init__(self):
        super(Cart, self).__init__(CartModel)

    def insert(self, **kwargs):
        return super(Cart, self).insert(tags=[], rating=None, **kwargs)

    # Get by tag function
    def get_by_tag(self, label):
        return [item for item in self.find() if label in item.tags]
