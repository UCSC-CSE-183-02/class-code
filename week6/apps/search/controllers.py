
from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash


@action("index")
@action.uses("index.html", auth)
def index():
    return dict()

@action("countries")
@action.uses(db)
def countries():
    text = request.GET.get("text", "")
    rows = db(db.country.name.contains(text)).select()
    return {"countries": rows.as_list()}