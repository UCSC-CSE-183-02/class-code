from .common import db, Field
from pydal.validators import *

db.define_table("todo", 
                Field("what", requires=IS_NOT_EMPTY()),
                Field("when", "datetime"))