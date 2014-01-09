# Models and Collections for users
from website.models.base import Collection, Model
from website.models.review import Review


''' Format for an insert would be:
    users.insert(username=...,password=...,is_owner=...)
'''
class UserModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(UserModel, self).__init__(db, fs, collection, obj)

    # Change password with authentication
    def change_password(self, oldpass, newpass, confirm):
        if oldpass == self.password:
            if newpass == confirm:
                self.password = newpass
                self.save()
                return True
        return False

    # Change password with authentication
    def change_username(self, password, newusr):
        if password == self.password and not self.collection.exists(newusr):
            self.username = newusr
            self.save()
            return True
        return False

    # Get blog reviews made by this user, and with other arguments
    def get_reviews(self, **kwargs):
        reviews = Review()
        return reviews.find(user=self.username, **kwargs)


class User(Collection):

    def __init__(self):
        super(User, self).__init__(UserModel)

    def insert(self, **kwargs):
        return super(User, self).insert(**kwargs)

    # Checks if a specific user exists
    def exists(self, username):
        return self.find_one(username=username) is not None
