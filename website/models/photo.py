from website.models.base import Collection, Model
from datetime import datetime


class PhotoModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(PhotoModel, self).__init__(db, fs, collection, obj)

    def read(self):
        image = self.fs.get(self.get_id())
        data = image.read()
        image.close()
        return data


class Photo(Collection):

    def __init__(self):
        super(Photo, self).__init__(PhotoModel)

    def insert(self, image_file, **kwargs):
        image_id = self.fs.put(image_file.read())
        return super(Photo, self).insert(_id=image_id, date_added=datetime.now(), url_path='/_image/%s' % str(image_id), **kwargs)
