from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

book_db = [

    {'id': 0, 'title': 'op'},
    {'id': 1, 'title': 'op2'},
    {'id': 2, 'title': 'op3'},


]

@api.route('/books')
class BookList(Resource):
    def get(self,):
        return book_db