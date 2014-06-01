import random
import string
import hashlib
import cherrypy

import lib.mako_templating
from lib.models.models import User, session_scope

class Login(object):
    @cherrypy.expose
    @cherrypy.tools.template(template="template/login.mako")
    def index(self, login = None, email = None, password = None):
        if email and password:
            with session_scope() as s:
                user = User.query_by_email_address(s, email)
            if user:
                cherrypy.session["user_id"] = user.id.decode("UTF-8")
        cherrypy.response.status = 200