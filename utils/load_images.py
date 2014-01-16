from website.models import Photo
import os

photos = Photo()

def load_images():
    photo_dir = "website/static/images"
    fnames = [os.path.realpath(os.path.join(root, name)) for (root, dirs, files) in os.walk(photo_dir) for name in files]
    for name in fnames:
        f = open(name, 'r')
        fields = name.split('/')
        title = fields[len(fields) - 1]

        if name == '.DS_Store':
            continue

        if not title in ['.DS_Store', 'search-icon.png']:
            photos.insert(image_file=f, is_cart=True, title=title)
            f.close()
        else:
            photos.insert(image_file=f, is_cart=False, title=title)
            f.close()
