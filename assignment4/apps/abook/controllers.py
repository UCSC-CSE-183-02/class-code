import uuid

from py4web import URL, Field, abort, action, redirect, request
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.url_signer import URLSigner

from .common import T, auth, cache, db, session, signed_url

url_signer = URLSigner(session)

# The auth.user below forces login.
@action("index")
@action.uses("index.html", auth.user)
def index():
    return dict()
