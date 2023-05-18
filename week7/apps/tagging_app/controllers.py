from py4web import action, request, abort, redirect, URL, HTTP
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.form import Form
from .models import thing_features

@action("index")
@action.uses("generic.html", auth, T)
def index():
    return locals()

@action("api/create_thing", method="POST")
@action.uses(auth)
def index():
    data = request.json  # {"name": "chair", "features": ["red", "short"]}
    print(data)
    name = data.get("name")
    features = data.get("features")
    if not name or not isinstance(features, list): raise HTTP(400)
    # check that features if a list
    id = db.thing.insert(name=name)
    thing_features.add(id, features)
    return "ok"
