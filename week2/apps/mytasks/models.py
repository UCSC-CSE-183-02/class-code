"""
This file defines the database models
"""

from .common import db, Field, auth
from pydal.validators import *
import datetime

STATUSES = ("pending", "completed", "rejected")

db.define_table(
    "task",
    Field("title", requires=IS_NOT_EMPTY()),
    Field("description", "text"),
    Field("deadline", "datetime"),
    Field("assignee", "reference auth_user", default=lambda: auth.user_id),
    Field("status", requires=IS_IN_SET(STATUSES), default="pending"),
    auth.signature
)

db.define_table(
    "comment",
    Field("task_id", "reference task", writable=False, readable=False),
    Field("body", label="Your Message"),
    auth.signature
)

db.commit()

