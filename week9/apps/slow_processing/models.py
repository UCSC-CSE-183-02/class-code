"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *

db.define_table(
    "document",
    Field('content', 'upload'),
    Field('status', writable=False, readable=False, requires=IS_IN_SET(['uploaded', 'processing', 'processed','failed']))
)

db.commit()

