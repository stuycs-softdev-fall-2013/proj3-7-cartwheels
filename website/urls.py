from website import app, views

# Home
app.add_url_rule('/', view_func=views.index)

# Carts
app.add_url_rule('/carts/<cid>', view_func=views.cart_page, methods=['GET', 'POST'])
app.add_url_rule('/carts/<cid>/manage', view_func=views.manage_cart, methods=['GET', 'POST'])

# Users
app.add_url_rule('/users/<username>', view_func=views.user_page, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=views.logout)
app.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'])

# Data
app.add_url_rule('/_data', view_func=views.serve_carts)
app.add_url_rule('/_image/<image_id>', view_func=views.serve_image)
