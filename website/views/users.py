from flask import session, redirect, url_for
from website import app
from utils import base_context


# Cart page
@app.route('/users/username', methods=['GET', 'POST'])
def user_page(username):
    context = base_context()
    pass


# Logout
@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect(url_for('home'))
