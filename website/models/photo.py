from website.models.base import Collection, Model


class PhotoModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(PhotoModel, self).__init__(db, fs, collection, obj)


class Photo(Collection):

    def __init__(self):
        super(Photo, self).__init__(PhotoModel)

    def insert(self, **kwargs):
        return super(Photo, self).insert(**kwargs)
