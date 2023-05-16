"""
This file defines the database models
"""

from .common import db, Field, auth
from pydal.validators import *

db.define_table(
    "product",
    Field("name"),
    Field("description", "text"),
    Field("unit_price", "float"),
    Field("picture", "upload"),
)

db.define_table(
    "order_item",
    Field("product_id", "reference product"),
    Field("quantity", "integer"),
    Field("unit_price", "float"),
    auth.signature,
)

db.commit()

