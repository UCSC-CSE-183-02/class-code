from py4web import action, request


@action("index", method=["GET", "POST"])
def index():
   return f"""
   <html>
   <body>
   Hello World {request.method} {request.GET} {request.POST}
   <form method="POST">
   <input name="x"/>
   <input type="submit"/>
   </form>
   </body>
   </html>
   """
