"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *

db.define_table("person", Field("name"))

db.commit()

if db(db.person).count() == 0:
    import random
    from py4web.utils.populate import FIRST_NAMES
    for k in range(100):
        db.person.insert(name=random.choice(FIRST_NAMES))
    db.commit()
        