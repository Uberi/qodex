import os
import json
import cherrypy

BASE_PATH = os.path.abspath(os.getcwd())

import lib.login
import lib.mako_templating
import lib.user_page

cherrypy.tools.user = lib.user_page.UserTool()

from lib.models.models import User, Group, Book, session_scope

class Users(object):
    @cherrypy.expose
    def index(self, filter = ""):
        with session_scope() as s:
            return json.dumps(User.list(s, filter))
    
    @cherrypy.expose
    def create(self, name, password, email, latitude, longitude):
        user = User(name, password, email, latitude, longitude)
        with session_scope() as s:
            s.add(user)

    @cherrypy.expose
    @cherrypy.tools.user()
    def logout(self):
        user = cherrypy.request.user
        del cherrypy.session["user_id"]

    @cherrypy.expose
    @cherrypy.tools.user()
    def delete(self):
        user = cherrypy.request.user
        with session_scope() as s:
            s.delete(user)

class Qodex(object):
    def __init__(self):
        self.login = lib.login.Login()
        self.users = Users()

    @cherrypy.expose
    def index(self):
        return cherrypy.lib.static.serve_file(os.path.join(BASE_PATH, "./static/index.html"))
    
    @cherrypy.expose
    def groups(self, filter = ""):
        with session_scope() as s:
            return json.dumps(Group.list(s, filter))

if __name__ == "__main__":
    configuration = {
        "/": {
            "tools.sessions.on": True,
            "tools.staticdir.root": BASE_PATH,
        },
        "/static": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": "./static",
        },
        "/favicon.ico": {
          "tools.staticfile.on": True,
          "tools.staticfile.filename": os.path.join(BASE_PATH, "./favicon.ico"),
        },
    }
    cherrypy.config.update("config.cfg")
    cherrypy.quickstart(Qodex(), "/", configuration)
