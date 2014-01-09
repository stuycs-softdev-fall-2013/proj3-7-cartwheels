from flask import session, redirect, url_for
from utils import base_context


# User page
def user_page(username):
    context = base_context()
    pass


# Logout
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect(url_for('home'))
