import socket
import os
import sys
import traceback

def is_safe(filename):
    """make sure only serve files from inside the static folder"""
    return os.path.normpath(filename) == filename and filename.startswith("static/")

def response_ok(http_body, mime_type):
    http_headers = [
        "HTTP/1.1 200 OK",
        "Content-Type: %s; charset=utf-8" % mime_type,
        "Content-Length: %s" % len(http_body),
        "Content-Language: en-US",
        "Date: Thu, 06 Dec 2018 17:37:18 GMT",
        "Server: my-very-own-little-server",
        ""
    ]
    return "\r\n".join(http_headers).encode() + b"\r\n" + http_body

def response_404():
    return b"HTTP/1.1 404 FILE NOT FOUNDr\\n\r\n"

def response_500():
    return b"HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\n"

MIME_TYPES = {
    "jpeg": "image/jpeg",
    "png": "image/png",
    "mp3": "audio/mp3",
    "mov": "movie/mpeg4",
}

routes = {}

def action(url):
    def wrapper(f):
        routes[url] = f
        return f
    return wrapper
   

def main(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(("0.0.0.0", port))

    sock.listen(1)

    while True:
        (conn, address) = sock.accept()
        print(address)
        request = conn.recv(10000).decode()
        lines = request.split('\r\n')
        a,b,c = lines[0].split() # GET /index?q=hello HTTP/1.1
        parts = b.split("?", 1)
        filename = parts[0]
        query_string = parts[1] if len(parts) > 1 else None

        if filename in routes:
            try:
                output = routes[filename](query_string)
            except:
                output = f"<html><body><pre>{traceback.format_exc()}</pre></body></html>"
            conn.send(response_ok(output.encode(), "text/html"))
            conn.close()
            continue

        if filename == '/':
            filename = "/index.html"
        filename = "static" + filename
        extension = filename.split(".")[-1]
        if not os.path.exists(filename) or not is_safe(filename): 
            conn.send(response_404())
        else:
            print(filename)
            with open(filename, "rb") as stream:
                http_body = stream.read()
            if extension in MIME_TYPES:
                conn.send(response_ok(http_body, MIME_TYPES[extension]))
            else:
                conn.send(response_ok(http_body, "text/html"))
        conn.close()


@action("/index.html")
def index(request):
    return "hello world"

@action("/test1.html")
def index(request):
    return "hello test1"

if __name__ == "__main__":
    main(port=int(sys.argv[1]))