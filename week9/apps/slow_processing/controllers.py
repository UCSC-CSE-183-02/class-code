from py4web import action, request, abort, redirect, URL, Field
from pydal.validators import IS_IN_SET
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.form import Form

import time

@action("index", method=["GET", "POST"])
@action.uses("index.html", auth, T)
def index():
    db.document.status.default = "uploaded"
    form = Form(db.document)
    if form.accepted:
        return dict(message = f"Your document is being processed", form=None)
    return dict(form=form, message=None)

@action("api/documents")
@action.uses(auth)
def api_documents():
    rows = db(db.document).select().as_list()
    return dict(documents=rows)