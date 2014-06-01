import os
import random
import string
import hashlib
import cherrypy

import lib.mako_templating
from lib.models.models import User, session_scope

class Login(object):
    @cherrypy.expose
    def index(self, login = None, email = None, password = None, next = None):
        if email and password:
            with session_scope() as s:
                user = User.query_by_email(s, email)
                if user:
                    cherrypy.session["user_id"] = user.id
            next = cherrypy.session["next"] if "next" in cherrypy.session else "/"
            raise cherrypy.HTTPRedirect(next)
        else:
            cherrypy.session["next"] = next
            return cherrypy.lib.static.serve_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../static/login/index.html"))
