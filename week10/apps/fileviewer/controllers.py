from py4web import action, response
import os

@action("index")
@action.uses("index.html")
def index():
    return dict()

def get_files(path="."):
    files = []
    for item in os.listdir(path):
        fullpath = os.path.join(path, item)
        if os.path.isdir(fullpath):
            typ = "folder"
        else:
            typ = "file"
        size = os.path.getsize(fullpath)
        mtime = os.path.getmtime(fullpath)
        info = {"name": item, "fullpath": fullpath, "type": typ, "size": size, "mtime": mtime}
        if typ == "folder":
            info["content"] = get_files(os.path.join(path, item))
        files.append(info)
    return files

@action("api/files")
def api_files():
    path = "."
    return dict(files=get_files(path))

@action("api/file/<path:path>")
def api_file(path):
    response.headers["Content-Type"] = "text"
    with open(path) as stream:
        return stream.read()


