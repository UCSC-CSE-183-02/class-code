

from py4web import action, request, abort, redirect, URL
from .common import db, session, T, auth
from py4web.utils.form import Form
import datetime

@action("index")
@action.uses("index.html", auth)
def index():    
    return dict()

@action("main", method=["GET", "POST"])
@action.uses("main.html", auth.user)
def main():    
    # lists my tasks and let me create a new task
    form = Form(db.task)
    tasks = db(db.task).select()
    return dict(form=form, tasks=tasks)

@action("details/<task_id>", method=["GET", "POST"])
@action.uses("details.html", auth.user)
def details(task_id): 
    # details about a task and can comment about the task
    my_task = db.task[task_id]   
    db.comment.task_id.default = task_id
    form = Form(db.comment)
    comments = db(db.comment.task_id==task_id).select(
        orderby=~db.comment.created_on
    )
    return dict(my_task=my_task, form=form, comments=comments)

@action("edit/<task_id>")
@action.uses("generic.html", auth.user)
def edit(task_id):    
    # edit a task
    form = Form(db.task, task_id)
    return dict(form=form)



