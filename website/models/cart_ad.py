from website.models.base import Model, Collection
from website.models.photo import Photo
import random


photos = Photo()


''' Format for an insert would be:
    carts.insert(cart_id=...,photo_id=...,priority=[1,5])
'''
class CartAdModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(CartAdModel, self).__init__(db, fs, collection, obj)


    def get_image(self):
        return photos.find_one(_id=self.photo_id)


class CartAd(Collection):

    def __init__(self):
        super(CartAd, self).__init__(CartAdModel)

    # Get a random add, handicapped torwards higher priority
    def get_random(self):
        results = self.find()
        baseline = int(random.random() * 5)
        results = [r for r in results if r.priority > baseline]
        random.shuffle(results)
        return results[0]
