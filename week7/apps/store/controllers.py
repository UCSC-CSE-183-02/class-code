
from py4web import action, request, abort, redirect, URL, HTTP
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.grid import Grid
import json

@action("index")
@action.uses("index.html", auth, T)
def index():
    return dict(json=json)


@action("manage/<path:path>", method=["GET","POST"])
@action.uses("generic.html", auth.user, T)
def manage(path):
    if auth.user_id != 1:
        raise HTTP(401)
    grid = Grid(path, db.product)
    return locals()

@action("api/products")
@action.uses(auth)
def api_products():
    products = db(db.product).select().as_list()
    return dict(products=products)

# @action("api/order_one_product", method="POST")
# @action.uses(auth)
# def api_order_one_product():
#     data = request.json
#     product_id=data.get("product_id")
#     quantity=data.get("quantity")
#     product = db.product[product_id]
#     db.order_item.insert(product_id=product_id,
#                          quantity=quantity,
#                          unit_price=product.unit_price)
#     return dict()


@action("api/buy_cart", method="POST")
@action.uses(auth)
def api_make_order():
    data = request.json
    print(data)
    for product_request in data.values():       
        product_id = product_request.get("id")
        quantity = product_request.get("quantity")
        product = db.product[product_id]
        db.order_item.insert(product_id=product_id,
                             quantity=quantity,
                             unit_price=product.unit_price)
    return dict()
