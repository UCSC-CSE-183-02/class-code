from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash


@action("index")
@action.uses("index.html", auth, T)
def index():
    return dict()

@action("api/users")
@action.uses(db)
def api_users():
    users = db(db.auth_user).select(db.auth_user.id, db.auth_user.first_name, db.auth_user.last_name)
    return dict(users = users.as_list())

