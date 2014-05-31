# -*- coding: utf-8 -*-
import cherrypy
import urllib.parse

from lib.database import User

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
        login_url = "/login?next=%s" % urllib.parse.urlencode(cherrypy.url())
        if 'user_id' in cherrypy.session: # not authenticated
            raise cherrypy.HTTPRedirect(login_url)
        user = User.query_by_id(cherrypy.session['user_id'])
        if not user: # invalid user ID
            raise cherrypy.HTTPRedirect(login_url)
        cherrypy.request.user = user # store the user for the request

    def _cleanup(self):
        cherrypy.request.user = None