Read more info about HTTP:

https://developer.mozilla.org/en-US/docs/Web/HTTP/Session

# Url parsing

    URL: http://example.com:80/index#something?name=hello
         ====   =========== == ===== ========= ==========
    http or https (scheme)
    example.com   (domain name) -> 127.0.0.1 (ipv4 address aka AF_INET)
    80            (port for http)
    443           (port for https - ssl)
    /index        (path_info)
    ?name=hello   (query_string)
    #something    (hash)

# Example HTTP client

    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect(("www.python.org", 80))

# Example HTTP server

    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind((socket.gethostname(), 80))
    # become a server socket listening to up to 1 client
    serversocket.listen(1)
    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
	data = clientsocket.recv(10000)
	response = "..."
	clientsocket.send(response)	

# HTTP Status codes

https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

200 OK
404 NOT FOUND
500 INTERNAL SERVER ERROR

Python as a web server:
https://www.digitalocean.com/community/tutorials/python-simplehttpserver-http-server

More python web servers:
https://geekflare.com/python-web-servers/
https://github.com/web2py/rocket3

Non-python web server:
https://www.nginx.com/

HTML tutorial: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics 

CSS tutorial: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics

Bulma tutorial: https://www.freecodecamp.org/news/learn-bulma-in-5-minutes-ec5188c53e83/