
from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash


@action("index")
@action.uses("index.html", auth, T)
def index():
    return dict()

@action("main")
@action.uses("main.html", auth.user, T)
def main():    
    return dict()

# API for get list of users
@action("users")
@action.uses(auth.user)
def users():
    rows = db(db.auth_user).select(
        db.auth_user.id, db.auth_user.first_name, db.auth_user.last_name
    ).as_list()
    return dict(users=rows)

# API to get list of my tasks
@action("my_tasks")
@action.uses(auth.user)
def my_task():
    me = auth.user_id
    query = (db.task.assigned_to == me) | (db.task.created_by == me)
    rows = db(query).select(orderby=~db.task.deadline|~db.task.created_on).as_list()
    return dict(my_tasks=rows)

# API to post new_task
@action("post_new_task", method="POST")
@action.uses(auth.user)
def post_new_task():
    db.task.validate_and_insert(**request.json)
    return dict()


# API to change the status of a task
# API to post new_task
@action("update_task", method="PUT")
@action.uses(auth.user)
def update_task():
    task = request.json
    task_id = task.get("id")
    task_status = task.get("status")
    query = db.task.created_by==auth.user_id
    query |= db.task.assigned_to==auth.user_id
    query &= db.task.id == task_id
    db(query).validate_and_update(status=task_status)
    return dict()
