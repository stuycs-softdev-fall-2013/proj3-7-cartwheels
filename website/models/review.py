# Models and Collections for reviews
from website.models.base import Collection, Model


''' Format for an insert would be:
    reviews.insert(text=...,rating=...,user=...,cart_id=...)
'''
class ReviewModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(ReviewModel, self).__init__(db, fs, collection, obj)


class Review(Collection):

    def __init__(self):
        super(Review, self).__init__(ReviewModel)

    def insert(self, **kwargs):
        return super(Review, self).insert(**kwargs)
