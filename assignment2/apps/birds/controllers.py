from py4web import action, request, abort, redirect, URL
from .common import db, session, T, cache, auth, logger
from .models import get_user_email

@action('index')
@action.uses('index.html', auth)
def index():
    ### You have to modify the code here as well.
    return dict()
