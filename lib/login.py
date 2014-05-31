import random
import string
import hashlib
import cherrypy

import lib.mako_templating

class Login(object):
    @cherrypy.expose
    @cherrypy.tools.template(template="template/login.mako")
    def index(self):
        cherrypy.response.status = 200

    @cherrypy.expose
    def display(self):
        return cherrypy.session["mystring"]