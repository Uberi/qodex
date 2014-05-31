import os
import cherrypy

BASE_PATH = os.path.abspath(os.getcwd())

import lib.login
import lib.mako_templating
import lib.user_page

class Qodex(object):
    def __init__(self):
        self.login = lib.login.Login()

if __name__ == "__main__":
    configuration = {
        "/": {
            "tools.sessions.on": True,
            "tools.staticdir.root": BASE_PATH,
            "tools.staticfile.on": True,
            "tools.staticfile.filename": os.path.join(BASE_PATH, "./static/index.html"),
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
