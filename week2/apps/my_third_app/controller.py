
from py4web import action, redirect, URL, HTTP, request

@action("index")
@action.uses("index.html")
def index():    
    return dict(msg = f"Hello from my third app")