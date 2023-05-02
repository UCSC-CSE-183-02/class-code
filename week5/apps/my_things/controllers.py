
from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash


@action("index")
@action.uses("index.html", auth, T)
def index():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    actions = {"allowed_actions": auth.param.allowed_actions}
    return dict(message=message, actions=actions)

@action("thing", method="GET")
@action.uses(db, auth)
def thing():
    rows = db(db.thing).select().as_list()
    return {"things": rows}

@action("thing/<id:int>", method="GET")
@action.uses(db, auth)
def thing(id):
    row = db.thing[id]
    return row.as_dict()

@action("thing", method="POST")
@action.uses(db, auth)
def thing():
    data = request.json
    db.thing.insert(name=data["name"])
    return {"things": []}

@action("thing/<id:int>", method="DELETE")
@action.uses(db, auth)
def thing(id):
    del db.thing[id]
    return {"status": "ok"}

@action("thing/<id:int>", method="PUT")
@action.uses(db, auth)
def thing(id):
    data = request.json
    db(db.thing.id==id).update(name=data['name'])
    return {"status": "ok"}
