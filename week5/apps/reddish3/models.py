from .common import db, Field
from pydal.validators import *

from . common import auth

db.define_table(
    "post",
    Field("title", "string", requires=IS_NOT_EMPTY()),
    Field("url", "string", requires=IS_EMPTY_OR(IS_URL())),
    Field("body", "text"),
    Field("score", "integer",writable=False,readable=False),
    auth.signature
)

db.define_table(
    "comment",
    Field("post_id", "reference post", writable=False),
    Field("body", "text"),
    auth.signature
)

db.commit()
