"""
This file defines the database models
"""

from .common import db, Field, auth
from pydal.validators import *

db.define_table(
    "task",
    Field("body", requires=IS_NOT_EMPTY()),
    Field("status", requires=IS_IN_SET(["pending", "completed", "rejected"])),
    Field("assigned_to", "reference auth_user"),
    Field("deadline", "datetime", IS_DATETIME()),
    auth.signature
)

if db(db.auth_user).count() == 1:
    from py4web.utils.populate import populate
    populate(db.auth_user, 10)
    populate(db.task, 100)

db.commit()    
