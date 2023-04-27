
from py4web import action, request, abort, redirect, URL, HTTP
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash


@action("index")
@action.uses("index.html", auth, T)
def index():
    user = auth.get_user()
    message = T("Hello {first_name}".format(**user) if user else "Hello")
    actions = {"allowed_actions": auth.param.allowed_actions}
    return dict(message=message, actions=actions)

@action("people")
@action.uses("people.html", db, auth)
def index():
    N = 5
    try:
        page = int(request.GET.get("page", 0))
    except:
        raise HTTP(404)
    rows = db(db.person).select(limitby=(N*page, N*page+N))
    return locals()
