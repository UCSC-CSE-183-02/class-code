from py4web import action, request, abort, redirect, URL, Field
from .common import db, session, T, cache, auth, logger
from py4web.utils.form import Form
from pydal.validators import IS_NOT_EMPTY

@action("index")
@action.uses("index.html")
def index():
    return dict(message="hello")

@action("hello")
@action.uses("generic.html", auth.user)
def hello():    
    return dict(message=f"Hello")

@action("todo", method=["GET", "POST"])
@action.uses("todo.html", auth.user)
def todo():    
    form = Form(db.todo)
    items = db(db.todo).select()
    return dict(form=form, items=items)
