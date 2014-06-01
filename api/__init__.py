import json
from lib.models import models
import cherrypy

import lib.user_page
cherrypy.tools.user = lib.user_page.UserTool()

from lib.models.models import User, Group, Book, session_scope
from api.json_responses import dict_user, jsonify_user, dict_group, jsonify_group, dict_book, jsonify_book

# RESTful API
class UserAPI(object):
    @cherrypy.expose
    def index(self, filter = ""):
        with session_scope() as s:
            return json.dumps(dict_user(user) for user in [User.list(s, filter)])

    @cherrypy.expose
    def create(self, name, password, email, latitude, longitude, bio):
        user = User(name, password, email, latitude, longitude, bio)
        with session_scope() as s:
            s.add(user)
            return "OK"
        return "FAIL"

    @cherrypy.expose
    @cherrypy.tools.user()
    def logout(self):
        user = cherrypy.request.user
        del cherrypy.session["user_id"]
        return "OK"

    @cherrypy.expose
    @cherrypy.tools.user()
    def delete(self):
        user = cherrypy.request.user
        with session_scope() as s:
            s.delete(user)
            return "OK"
        return "FAIL"
    
    def join(self, group_id):
        user = cherrypy.request.user
        group = Group.query_by_id(group_id)
        with session_scope() as s:
            user.join_group(s, group)
    
    def leave(self, group_id):
        user = cherrypy.request.user
        group = Group.query_by_id(group_id)
        with session_scope() as s:
            user.leave_group(s, group)

class GroupAPI(object):
    @cherrypy.expose
    def index(self, filter = ""):
        with session_scope() as s:
            return json.dumps([dict_group(group) for group in Group.list(s, filter)])

    @cherrypy.expose
    def create(self, title, password):
        group = Group(title, password)
        with session_scope() as s:
            s.add(group)
            return "OK"
        return "FAIL"
    
    @cherrypy.expose
    def title(self, group_id):
        group = Group.query_by_id(group_id)
        return group.title
    
    @cherrypy.expose
    def add_book(self, group_id, book_id):
        group = Group.query_by_id(group_id)
        book = Book.query_by_id(book_id)
        group.add_book(book)
        return "OK"

    @cherrypy.expose
    def remove_book(self, group_id, book_id):
        group = Group.query_by_id(group_id)
        book = Book.query_by_id(book_id)
        group.remove_book(book)
        return "OK"

class BookAPI(object):
    @cherrypy.expose
    def index(self, filter = ""):
        with session_scope() as s:
            return json.dumps([dict_book(book) for book in Book.list(s, filter)])

    @cherrypy.expose
    def create(self, title, isbn, author):
        book = Book(title, isbn, author)
        with session_scope() as s:
            s.add(book)
            return "OK"
        return "FAIL"