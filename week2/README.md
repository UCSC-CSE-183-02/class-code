
# what our program does

- web server and can return files
- routing: it can map URLs into function calls
- parse request: pass the request to the functions

# what do frameworks do (server side)

- handle concurrenty
- can interface with other web servers (cherrypy, rocket3, twisted, gunicorn, ...) WSGI
- routing: it can map URLs into function calls
- parse request: pass the request to the functions
- cache: store pages or partial data for reuse and speed
- session: store information associated to each client
- cookies: set cookies and retrieve cookies
- authentication: id users (login, register, logout, lost password)
  - sso
- authorization: what can the user do?
- database intraction (sqlalchemy, pydal)
- database abstraction (sqlalchemy, pydal)
- internationalization (i18n)
- pluralization (i11n)
- templating
- model-view-controller architecture

# specific of py4web

- can handle multiple applications at the same time
- web based IDE (Django does it also)
- ticket handling
- generates forms from database

# Basic functions in py4web

- action("index")
- action.uses("index.html", auth)
- redirect(...)
- URL(...)
- raise HTTP(404)
- request.url, request.method, request.GET, request.POST, request.json

# Basic fixtures

  (class)       (instance)
- Session    => session
- Translator => T
- Auth       => auth, auth.user
- URLSigner  => url_signer

# pydal API

- DAL
- Field
- db.table.insert(....)
- db(query).select(...)
- db(query).update(...)
- db(query).delete()

# dashboard template

https://vikdiesel.github.io/admin-one-bulma-dashboard/tables.html