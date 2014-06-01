import json
from lib.models import models
import cherrypy

import lib.user_page
cherrypy.tools.user = lib.user_page.UserTool()

from lib.models.models import User, Group, Book, session_scope

def dict_user(user):
	# TODO: add list of groups the user is in to the json
	with session_scope() as s:
		return {'id':user.id, 'email':user.email, 'latitude':user.latitude, 'longitude':user.longitude, 'bio':user.bio, 'groups':user.groups}

def jsonify_user(user):
	return json.dumps(dict_user(user))

def dict_book(book):
	return {'id':book.id, 'title':book.title, 'isbn':book.isbn, 'author':book.author}

def jsonify_book(group):
	return json.dumps(dict_book(book))

def dict_group(group):
	with session_scope() as s:
		return {'id':group.id, 'book_list': group.book_list(s), 'user_list': group.user_list(s)}

def jsonify_group(group):
	return json.dumps(dict_group(group))

def jsonify_error(errno, errmsg):
	return json.dumps({'error':{'code':errno,'message':errmsg}})