import os
import json
import cherrypy

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

import lib.login
import api

class Qodex(object):
    def __init__(self):
        self.login = lib.login.Login()
        self.users = api.UserAPI()

    @cherrypy.expose
    def index(self):
        return cherrypy.lib.static.serve_file(os.path.join(BASE_PATH, "static/index.html"))
    
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
