import json
from lib.models import models
import cherrypy

import lib.user_page
cherrypy.tools.user = lib.user_page.UserTool()

from lib.models.models import User, Group, Book, session_scope

def dict_user(user):
	return {('user%s' % user.id):{'id':user.id, 'email':user.email, 'latitude':user.latitude, 'longitude':user.longitude}}

def jsonify_user(user):
	return json.dumps({('user%s' % user.id):{'id':user.id, 'email':user.email, 'latitude':user.latitude, 'longitude':user.longitude}})

def jsonify_book(book):
	return json.dumps({('book%s' % book.id):{'id':book.id, 'title':book.title, 'isbn':book.isbn, 'author':book.author}})