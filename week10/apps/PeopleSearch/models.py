"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *
from py4web.utils.populate import populate

if db(db.auth_user).count() == 0:
    populate(db.auth_user, 100)

db.commit()

