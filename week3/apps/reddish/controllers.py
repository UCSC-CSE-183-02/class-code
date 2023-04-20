from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.form import Form, FormStyleBulma

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



