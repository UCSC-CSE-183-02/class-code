from py4web import action, request, HTTP
from .common import auth
import os

@action("index", method=["GET","POST"])
@action.uses("index.html", auth)
def index():
    if request.method == "POST":
        print("you uploaded:")
        target = "test"
        filename = request.files["doc_content"].filename
        # filename = ../../a/b/c/myfile.txt
        # myfile.txt
        # test/myfile.txt
        path = os.path.normpath(os.path.join(target, os.path.basename(filename)))
        if not path.startswith(target + "/"):
            raise HTTP(401)
        content = request.files["doc_content"].file.read()
        with open(path, "wb") as stream:
            stream.write(content)
    return dict()
