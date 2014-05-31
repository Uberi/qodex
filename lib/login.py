import random
import string
import hashlib
import cherrypy

import lib.mako_templating
from lib.database import User

class Login(object):
    @cherrypy.expose
    @cherrypy.tools.template(template="template/login.mako")
    def index(self, login = None, email = None, password = None):
        if email and password:
            user = User.query_by_email_address(email)
            if user:
                cherrypy.session["user_id"] = user.id.decode("UTF-8")
        cherrypy.response.status = 200