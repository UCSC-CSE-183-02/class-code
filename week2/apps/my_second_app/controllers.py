from py4web import action, request, abort, redirect, URL, Field
from .common import db, session, T, cache, auth, logger
from py4web.utils.form import Form
from pydal.validators import IS_NOT_EMPTY

@action("index")
@action.uses("index.html", auth)            # has access to auth
def index():
    return dict(message="hello")

@action("counter")
@action.uses(session)
def counter():
    session["c"] = session.get("c", 0) + 1  # add 1 to session["c"]
    return str(session["c"])

@action("hello")
@action.uses("generic.html", auth.user)    # requires an auth(enticated) user
def hello():    
    return dict(message=f"Hello")

@action("todo", method=["GET", "POST"])    # can process POSTed forms
@action.uses("todo.html", auth.user)       # requires an auth(enticated) user
def todo():    
    form = Form(db.todo)                   # make a create form for table db.todo
    items = db(db.todo).select()           # select records/items from table
    return dict(form=form, items=items)

