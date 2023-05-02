from py4web import action, request, abort, redirect, URL, Field, HTTP
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid

@action("index", method=["GET", "POST"])
@action.uses("index.html", auth)
def index():
    # form to post and list of posts    
    form = Form(db.post, formstyle=FormStyleBulma) if auth.user_id else None  
    rows = db(db.post).select(limitby=(0,100), orderby=~db.post.created_on)
    return locals()

@action("get_post/<post_id>", method=["GET", "POST"])
@action.uses("get_post.html", auth)
def get_post(post_id):
    row = db.post[post_id]
    db.comment.post_id.default = post_id
    form = Form(db.comment, formstyle=FormStyleBulma) if auth.user_id else None
    comments = db(db.comment.post_id==post_id).select(orderby=~db.comment.created_on)
    # details about the post_id and comments about post_id
    return locals()

@action("edit_post/<post_id>", method=["GET", "POST"])
@action.uses("generic.html", auth.user)
def edit_post(post_id):
    row = db.post[post_id]
    if not row or row.created_by != auth.user_id:
        raise HTTP(400)
    form = Form(db.post, row, formstyle=FormStyleBulma)
    # details about the post_id and comments about post_id
    return locals()

@action("manage/<tname>/<path:path>", method=["GET", "POST"])
@action.uses("manage.html", auth.user)
def manage(tname, path):
    # details about the post_id and comments about post_id
    grid = Grid(path, db[tname])
    return locals()
