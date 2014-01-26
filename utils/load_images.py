from website import photos
import os

def load_images():
    photos.remove_all()
    photo_dir = "website/static/images"
    fnames = [os.path.realpath(os.path.join(root, name)) \
            for (root, dirs, files) in os.walk(photo_dir) for name in files]

    for name in fnames:
        f = open(name, 'r')
        fields = name.split('/')
        title = fields[len(fields) - 1]

        if 'food_cart' in title:
            photos.insert(image_file=f, is_default=True, title=title)
            f.close()

        elif '.DS_Store' not in title:
            photos.insert(image_file=f, is_cart=True, title=title)
            f.close()

        else:
            photos.insert(image_file=f, is_cart=False, title=title)
            f.close()
