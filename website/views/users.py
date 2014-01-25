from flask import render_template, session, request, redirect, url_for
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
    context = base_context()
    if context['user'] is not None:
        session['username'] = None

    return redirect(url_for('index'))


# Login
def login():
    context = base_context()
    if context['user'] is not None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        form = request.form
        user = users.find_one(username=form['email'], password=form['pass'])

        if user is not None:
            session['username'] = user.username

        return redirect(url_for('index'))

    return render_template('login.html', **context)


# Register
def register():
    context = base_context()
    if context['user'] is not None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        form = request.form

        if form.has_key('user-submit'):
            first = form['first']
            last = form['last']
            email = form['email']
            password = form['pass']

            if users.find_one(username=email) is None:
                user = users.insert(first_name=first, last_name=last, username=email, password=password)
                session['username'] = user.username

            return redirect(url_for('index'))

        else:
            first = form['first']
            last = form['last']
            email = form['email']
            password = form['pass']

    return render_template('register.html', **context)
