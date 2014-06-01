# -*- coding: utf-8 -*-
import cherrypy
import urllib.parse

from lib.models.models import User, session_scope

__all__ = ['UserTool']

class UserTool(cherrypy.Tool):
    def __init__(self):
        """
        The user tool takes care of fetching the current
        logged in user to then associating it with
        the request.
        """
        cherrypy.Tool.__init__(self, 'before_handler', self._fetch, priority=20)

    def _setup(self):
        cherrypy.Tool._setup(self)
        cherrypy.request.hooks.attach('on_end_resource', self._cleanup, priority=80)

    def _fetch(self):
        login_url = "/login?next=%s" % urllib.parse.quote(cherrypy.url())
        if 'user_id' not in cherrypy.session: # not authenticated
            cherrypy.lib.cptools.redirect(login_url)
        
        with session_scope() as s:
            user = User.query_by_id(s, cherrypy.session['user_id'])
            if user:
                cherrypy.request.user_id = user.id # store the user for the request
            else: # invalid user ID
                cherrypy.lib.cptools.redirect(login_url)

    def _cleanup(self):
        cherrypy.request.user_id = None
