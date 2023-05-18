"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *
from pydal.tools.tags import Tags

db.define_table("thing", Field("name"))
thing_features = Tags(db.thing)

db.commit()

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#
