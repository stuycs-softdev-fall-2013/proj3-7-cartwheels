from website import app, views

# Home and search
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/search', view_func=views.search_results)

# Carts
app.add_url_rule('/carts/<cid>', view_func=views.cart_page, methods=['GET', 'POST'])
app.add_url_rule('/carts/<cid>/menu', view_func=views.menu_page, methods=['GET', 'POST'])
app.add_url_rule('/carts/<cid>/directions', view_func=views.directions, methods=['GET', 'POST'])

# Users
app.add_url_rule('/profile', view_func=views.profile, methods=['GET', 'POST'])
app.add_url_rule('/users/<uid>', view_func=views.user_profile, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=views.logout)
app.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'])

# Ads
app.add_url_rule('/ads', view_func=views.ads_page, methods=['GET', 'POST'])
app.add_url_rule('/ad/<name>', view_func=views.purchase_ad, methods=['GET', 'POST'])
# Data
# Data

app.add_url_rule('/_search', view_func=views.search_data)
app.add_url_rule('/_serve', view_func=views.serve_data)
app.add_url_rule('/_image/<image_id>', view_func=views.serve_image)
app.add_url_rule('/_image-default', view_func=views.serve_default)
