"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *

db.define_table(
    "follow",
    Field("follewed_id", "reference auth_user"),
    auth.signature
)

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
db.commit()
#
#
