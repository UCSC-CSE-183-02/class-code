from py4web import action
from .common import auth, T

@action("index")
@action.uses("index.html", auth, T)
def index():
    return dict(message=T("Hello World"))
