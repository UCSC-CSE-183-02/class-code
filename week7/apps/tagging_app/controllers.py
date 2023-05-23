from py4web import action, request, abort, redirect, URL, HTTP
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.form import Form
from .models import thing_features

@action("index")
@action.uses("index.html", auth, T)
def index():
    return locals()


@action("api/create_thing", method="POST")
@action.uses(auth)
def create_thing():
    data = request.json  # {"name": "chair", "features": ["red", "short"]}
    print(data)
    name = data.get("name")
    features = data.get("features")
    if not name or not isinstance(features, list): raise HTTP(400)
    # check that features if a list
    id = db.thing.insert(name=name)
    thing_features.add(id, features)
    return "ok"

@action("api/things")
@action.uses(db, session)
def things_by_tag():
    if "tags" in request.GET:
        tags = request.GET.get("tags").split(',')
        rows = db(thing_features.find(tags,mode="and")).select()
    else:
        rows = db(db.thing).select()
    rows = rows.as_list()
    for row in rows:
        row["features"] = thing_features.get(row["id"])
    return {"things": rows}
