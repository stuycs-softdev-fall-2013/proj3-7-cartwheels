from flask import render_template, session, request, redirect, url_for
from website import users, carts
from website.views.utils import base_context


# Own profile
def profile():
    context = base_context()
    if context['user'] is None:
        return redirect(url_for('index'))

    user = context['user']

    if user.is_owner:
        if request.method == 'POST':
            form = request.form
            cart = carts.find_one(permit_number=form['license'])
            cart.name = form['name']
            cart.zip_code = form['zip']
            cart.save()

        return render_template('owner_profile.html', **context)

    context['target_user'] = user
    return render_template('user_profile.html', **context)


# User page
def user_profile(uid):
    context = base_context()
    context['target_user'] = users.find_one(_id=uid)
    return render_template('user_profile.html', **context)


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

        else:
            context['error'] = 'Email and password combination is incorrect'


    return render_template('login.html', **context)


# Register
def register():
    context = base_context()
    if context['user'] is not None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        form = request.form

        if not form.has_key('license'):
            first = form['first']
            last = form['last']
            email = form['email']
            password = form['pass']

            if users.find_one(username=email) is None:
                user = users.insert(first_name=first, last_name=last,
                        username=email, password=password, is_owner=False)
                session['username'] = user.username
                return redirect(url_for('index'))

            else:
                context['error'] = 'Email already registered in the system'

        else:
            first = form['first']
            last = form['last']
            email = form['email']
            license = form['license']
            password = form['pass']

            if users.find_one(username=email) is None:
                user = users.insert(first_name=first, last_name=last,
                        username=email, password=password, licenses=[license],
                        is_owner=True)
                session['username'] = user.username
                return redirect(url_for('index'))

    return render_template('register.html', **context)
