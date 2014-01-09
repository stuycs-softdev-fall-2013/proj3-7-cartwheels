from website import app
from utils import base_context


# Cart page
@app.route('/carts/<cid>', methods=['GET', 'POST'])
def cart_page(cid):
    context = base_context()
    pass
