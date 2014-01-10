from flask import render_template, session, redirect, url_for
from utils import base_context


# User page
def user_page(username=None):
    context = base_context()
    return render_template('user.html', **context)


# Logout
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect(url_for('home'))


# Login
def login():
    context = base_context()
    if context['user'] is not None:
        return redirect(url_for('home'))

    return render_template('login.html', **context)


# Register
def register():
    context = base_context()
    if context['user'] is not None:
        return redirect(url_for('home'))

    return render_template('register.html', **context)
