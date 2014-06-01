import json
from lib.models import models

# RESTful API
class UserAPI(object):
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