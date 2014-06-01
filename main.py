import os
import json
import cherrypy

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

import lib.login
import lib.mako_templating
import api
from lib.models.models import User, session_scope

class Qodex(object):
    def __init__(self):
        self.login = lib.login.Login()
        self.users = api.UserAPI()
        self.groups = api.GroupAPI()
        self.books = api.BookAPI()

    @cherrypy.expose
    def index(self):
        return cherrypy.lib.static.serve_file(os.path.join(BASE_PATH, "static/index.html"))
    
    @cherrypy.expose
    @cherrypy.tools.user()
    @cherrypy.tools.template(template="templates/profile.mako")
    def profile(self):
        cherrypy.response.status = 200
        with session_scope() as s:
            user = User.query_by_id(s, cherrypy.request.user_id)
            cherrypy.session["variables"] = {"user_name": user.name, "user_email": user.email}
    
    @cherrypy.expose
    def groups(self, filter = ""):
        with session_scope() as s:
            return json.dumps(Group.list(s, filter))

if __name__ == "__main__":
    configuration = {
        "/": {
            "tools.sessions.on": True,
            "tools.staticdir.on": True,
            "tools.staticdir.dir": "./static",
            "tools.staticdir.root": BASE_PATH,
        },
        "/favicon.ico": {
          "tools.staticfile.on": True,
          "tools.staticfile.filename": os.path.join(BASE_PATH, "./favicon.ico"),
        },
    }
    cherrypy.config.update("config.cfg")
    cherrypy.quickstart(Qodex(), "/", configuration)
