from flask import render_template, session, redirect, url_for
from website import users
from website.views.utils import base_context


# Profile
def profile():
    context = base_context()
    if context['user'] is not None:
        return render_template('user.html', **context)

    return redirect(url_for('index'))


# User page
def user_page(username=None):
    context = base_context()
    context['target_user'] = users.find_one(username=username)
    return render_template('user.html', **context)


# Logout
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect(url_for('index'))


# Login
def login():
    context = base_context()
    if context['user'] is not None:
        return redirect(url_for('index'))

    return render_template('login.html', **context)


# Register
def register():
    context = base_context()
    if context['user'] is not None:
        return redirect(url_for('index'))

    return render_template('register.html', **context)
