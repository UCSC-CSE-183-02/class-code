
import datetime
import random

from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.url_signer import URLSigner
from .models import get_username

# Some constants.
MAX_RETURNED_USERS = 20 # Our searches do not return more than 20 users.
MAX_RESULTS = 20 # Maximum number of returned meows. 

@action('index')
@action.uses('index.html', db, auth.user)
def index():
    # lists all posts filtered by followed
    return dict()

@action("get_users")
@action.uses(db, auth.user)
def get_users():
    # Implement. Lists all the users 
    return dict()


@action("set_follow", method="POST")
@action.uses(db, auth.user)
def set_follow():
    # Implement.
    return "ok"
