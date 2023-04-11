from py4web import action

import random

@action("index")
def index():
    1/0
    return f"Hello World with random {random.randint(0,1000)}"
