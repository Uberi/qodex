import os, sys
import random
import string
import hashlib

import cherrypy
import lib.MakoTool
cherrypy.tools.render = lib.MakoTool.MakoTool()

class Qodex(object):
    @cherrypy.expose
    @cherrypy.tools.render(template="templates/index.mako")
    def index(self):
        cherrypy.response.status = 200

    @cherrypy.expose
    def generate(self, length=8):
        some_string = "".join(random.sample(string.hexdigits, int(length)))
        cherrypy.session["mystring"] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session["mystring"]

if __name__ == "__main__":
    configuration = {
        "/": {
            "tools.sessions.on": True,
            "tools.staticdir.root": os.path.abspath(os.getcwd()),

            #"server.ssl_module": "builtin",
            #"server.ssl_certificate": "./ssl/certificate.crt",
            #"server.ssl_private_key": "./ssl/private_key.key",
            #"server.ssl_certificate_chain": "./ssl/certificate_chain.crt",
        },
        "/static": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": "./static",
        }
    }
    cherrypy.quickstart(Qodex(), "/", configuration)
